from mavsdk import System
from mavsdk.offboard import PositionNedYaw
import asyncio

async def arm_and_takeoff(drone, altitude):
    print("Armando...")
    await drone.action.arm()

    print("Decolando...")
    await drone.action.set_takeoff_altitude(altitude)
    await drone.action.takeoff()

    await asyncio.sleep(5)

async def start_offboard(drone):
    print("Iniciando modo OFFBOARD")
    await drone.offboard.set_position_ned(PositionNedYaw(0.0, 0.0, -1.5, 0.0))
    await drone.offboard.start()

async def land(drone):
    print("Pousando...")
    await drone.action.land()