class seal:
	def __init__(seal, arm_length, leg_length, number_eyes, tail, furry):
		seal.arm_length = 0
		seal.leg_length = 0
		seal.number_eyes = 2
		seal.tail =  Yes
		seal.furry = Yes

def describe(seal):
	print(f"Seals are very fat and squishy and and super cute and they slap their stoamchs to assert their dominance")
	print(f"Arm Length: {seal.arm_length} unknown, I tried searching for it but I literally couldnt find it")
	print(f"Leg Length: {seal.leg_length} Unknown, they have flippers but the sizes weren't able to be found")
	print(f"Number of eyes: {seal.number_eyes} 2")
	print(f"Has a tail: {'Yes' if seal.tail else 'No'}")
	print(f"Is it furry: {'Yes' if seal.furry else 'No'}")

favorite_animal = seal(0, 0, 2, yes, yes)

favorite_animal.describe()

