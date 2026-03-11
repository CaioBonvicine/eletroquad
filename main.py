import asyncio
from mavsdk import System
from config import *
from flight_control import *
from vision import *
from command_server import *
from safety import *

async def run():

    drone = System()
    await drone.connect(system_address=CONNECTION_STRING)

    print("Conectando ao drone...")

    async for state in drone.core.connection_state():
        if state.is_connected:
            print("Drone conectado!")
            break

    print("Sistema pronto - aguardando START")

    while True:

        command = wait_for_command()

        if command == "START":

            print("Iniciando missão")

            await arm_and_takeoff(drone, TAKEOFF_ALTITUDE)
            await start_offboard(drone)

            camera = init_camera()

            if camera is None:
                print("Câmera não detectada! Abortando missão.")
                await land(drone)
                return
            asyncio.create_task(monitor_battery(drone))

            print("Buscando ArUco...")

            while True:
                aruco_id = detect_aruco(camera)

                if aruco_id is not None:
                    print("Alvo encontrado!")
                    break
            
            camera.release()
            await land(drone)
            await wait_until_landed(drone)

        elif command == "STOP":
            await emergency_land(drone)

asyncio.run(run())