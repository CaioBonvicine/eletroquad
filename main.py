import asyncio
from mavsdk import System
from config import *
from flight_control import *
from vision import *
from command_server import *
from safety import *
from utils import *

async def run():

    while True:
        try:
            print("\n[BOOT] Iniciando sistema...")

            drone = System()
            try:
                await drone.connect(system_address=CONNECTION_STRING)
            except Exception as e:
                print(f"[ERRO] Falha ao conectar: {e}")
                print("[RETRY] Tentando novamente em 10s...\n")
                await asyncio.sleep(10)
                continue
            connected = await wait_for_connection(drone)

            if not connected:
                print("[RETRY] Tentando novamente em 10s...\n")
                await asyncio.sleep(10)
                continue

            print("[OK] Sistema pronto - aguardando START")

            while True:

                command = wait_for_command()

                if command == "START":

                    print("[MISSÃO] Iniciando")

                    await arm_and_takeoff(drone, TAKEOFF_ALTITUDE)
                    await start_offboard(drone)

                    camera = init_camera()

                    if camera is None:
                        print("[ERRO] Câmera não detectada!")
                        await land(drone)
                        continue

                    asyncio.create_task(monitor_battery(drone))

                    print("[VISÃO] Buscando ArUco...")

                    while True:
                        aruco_id = detect_aruco(camera)

                        if aruco_id is not None:
                            print(f"[ALVO] Detectado ID {aruco_id}")
                            break

                        await asyncio.sleep(0.1)

                    camera.release()

                    await land(drone)
                    await wait_until_landed(drone)

                    print("[MISSÃO] Finalizada")

                elif command == "STOP":
                    print("[COMANDO] STOP recebido")
                    await emergency_land(drone)

        except Exception as e:
            print(f"[ERRO GLOBAL] {e}")

            try:
                print("[RECOVERY] Tentando pousar...")
                await land(drone)
            except:
                print("[RECOVERY] Falha ao pousar")

            print("[RESTART] Reiniciando em 10s...\n")
            await asyncio.sleep(10)


if __name__ == "__main__":
    asyncio.run(run())