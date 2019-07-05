class Generator:
	def __init__(self, class_reference, **kwargs):
		self.class_type = class_reference
		self.construction_kwargs = {}
		self.simple_kwargs = {}
		for arg, constructor in kwargs.items():
			if isinstance(constructor, Generator):
				self.construction_kwargs[arg] = constructor
			else:
				self.simple_kwargs[arg] = constructor

	def __call__(self, **specific_kwargs):
		final_args_dict = {}

		for arg, generator in self.construction_kwargs.items():
			final_args_dict[arg] = generator()

		for arg, value in self.simple_kwargs.items():
			final_args_dict[arg] = value

		for arg, value in specific_kwargs.items():
			final_args_dict[arg] = value

		return self.class_type(**final_args_dict)

class Container:
	def __init__(self):
		self.generators = []
	
	def __str__(self):
		dependencies = [g.class_type for g in self.generators]
		unique_generators = list(set(dependencies))
		dependencies_count = {unique_dependency: dependencies.count(unique_dependency)
				for unique_dependency in unique_generators}
		
		return str(dependencies_count)

	def add_generators(self, generators):
		self.generators += generators

class Engine:
	def __init__(self, brand):
		self.brand = brand

	def __str__(self):
		return str(self.__dict__)

class Car:
	def __init__(self, engine, car_id):
		self.engine = engine
		self.id = car_id

	def __str__(self):
		return str(self.__dict__)

if __name__ == "__main__":
	engine_generator_1 = Generator(Engine, brand='v8')
	engine_generator_2 = Generator(Engine, brand='diesel')
	#print(engine_generator_1.__dict__, engine_generator_2.__dict__, sep='\n')

	engine_1 = engine_generator_1()
	engine_2 = engine_generator_2()
	print(engine_1)
	print(engine_2)


	car_generator = Generator(Car, engine=engine_generator_1)
	#print(car_generator.__dict__)
	car_1 = car_generator(car_id='123')
	print(car_1)
	print(car_1.engine)


	main_container = Container()
	main_container.add_generators([engine_generator_1, engine_generator_2, car_generator])
	print(main_container)

