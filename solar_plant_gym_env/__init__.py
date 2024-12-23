from gymnasium.envs.registration import register

register(
    id="solar_plant_gym_env/SolarPlant-v0",
    entry_point="solar_plant_gym_env.envs:SolarPlant",
)
