import asyncio
from mavsdk.telemetry import LandedState

# -------------------------
# MONITORAMENTO DE BATERIA
# -------------------------

async def monitor_battery(drone, min_voltage=14.0):
    async for battery in drone.telemetry.battery():
        voltage = battery.voltage_v
        print(f"[BAT] Tensão: {voltage:.2f}V")

        if voltage <= min_voltage:
            print("[SAFETY] Tensão baixa! Pousando...")
            await drone.action.land()
            break

        await asyncio.sleep(1)


# -------------------------
# MONITORAMENTO DE LINK
# -------------------------

async def monitor_connection(drone):
    async for state in drone.core.connection_state():
        if not state.is_connected:
            print("[SAFETY] Conexão perdida!")
            break


# -------------------------
# FUNÇÃO DE EMERGÊNCIA
# -------------------------

async def emergency_land(drone):
    print("[EMERGÊNCIA] Pouso imediato acionado!")
    await drone.action.land()


# -------------------------
# VERIFICAR SE POUSOU
# -------------------------

async def wait_until_landed(drone):
    async for state in drone.telemetry.landed_state():
        if state == LandedState.ON_GROUND:
            print("[INFO] Drone pousado.")
            break