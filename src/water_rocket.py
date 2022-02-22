class WaterRocket():
    def __init__(
        self,
        # Rocket systems
        bottle_volume: float = 2.0,  # liters
        nozzle_diameter: float = 22,  # millimeters
        nozzle_efficiency: float = 70,  # percentage

        # Flight caracteristics
        mass_of_empty_rocket: float = 100,  # grammes
        drag_coef: float = 0.1,
        frontal_area: float = 0.008,  # square meters

        # Lauch configuration
        water_ratio: float = 40,  # % of volume
        initial_pressure: float = 2.5,  # bar

        # Laucher setup
        launch_angle: float = 45,  # degrees
        launch_tube_length: float = 0.20,  # meters
        launch_rail: bool = True,
        lauch_rail_length: float = 0.5,  # meters
    ) -> None:

        # Rocket systems
        self.bottle_volume = bottle_volume
        self.nozzle_diameter = nozzle_diameter
        self.nozzle_efficiency = nozzle_efficiency

        # Flight caracteristics
        self.mass_of_empty_rocket = mass_of_empty_rocket
        self.drag_coef = drag_coef
        self.frontal_area = frontal_area

        # Lauch configuration
        self.water_ratio = water_ratio
        self.initial_pressure = initial_pressure

        # Laucher setup
        self.launch_angle = launch_angle
        self.launch_tube_length = launch_tube_length
        self.launch_rail = launch_rail
        self.lauch_rail_length = lauch_rail_length
