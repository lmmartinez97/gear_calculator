from numpy import pi
import numpy as np

class SpurGear:
	""" 
	Class template of the spur gear object. Requests gear parameters and contains the necessary associations
	to determine the rest. This class is used as a tool to calculate transmission trains.

	The number of teeth must always be provided. The program determines whether module or pitch_diameter is 
	provided and calculates the other parameter. 
	"""
	def __init__(self, mod = 0, teeth = 0, pressure_angle = 20):
		self.mod = mod
		self.teeth = teeth
		self.pitch_diameter = pitch_diameter
		self.pressure_angle = pressure_angle
		self.pitch_diameter = self.mod * self.teeth
		
		#gear pitch
		self.circular_pitch = self.mod*pi
		self.diametral_pitch = 1/self.mod
		
		#gear geometrical parameters
		self.addendum = self.mod
		self.dedendum = 1.25*self.mod
		self.clearance = self.dedendum - self.addendum
		self.height = self.dedendum + self.addendum
		self.thickness = self.circular_pitch/2
		self.teeth_spacing = self.thickness

		self.width = 13*self.mod
		print("Spur gear width set to 13*m. Can be changed with the set_width() method by providing a factor betwen 10 and 16")

		#other diameters
		self.head_diameter = self.pitch_diameter + 2*self.mod
		self.base_diameter = self.pitch_diameter*np.cos(pressure_angle)
		self.root_diameter = self.pitch_diameter - 2.5*self.mod

	#width setter
	def set_width(width_factor):
		self.widht = width_factor*self.mod
	#getters
	def get_modulus(self):
		return self.mod

	def get_teeth_number(self):
		return self.teeth

	def get_pitch_diameter(self):
		return self.pitch_diameter

	def get_circular_pitch(self):
		return self.circular_pitch

	def get_diametral_pitch(self):
		return self.diametral_pitch

	def get_addendum(self):
		return self.addendum

	def get_dedendum(self):
		return self.dedendum

	def get_clearance(self):
		return self.clearance

	def get_height(self):
		return self.height

	def get_thickness(self):
		return self.thickness

	def get_teeth_spacing(self):
		return self.teeth_spacing

	def get_width(self):
		return self.width

	def get_head_diameter(self):
		return self.head_diameter

	def get_base_diameter(self):
		return self.base_diameter

	def get_root_diameter(self):
		return self.root_diameter


class HelicalGear():
	""" 
	Class template of the helical gear object. Requests gear parameters and contains the necessary associations
	to determine the rest. This class is used as a tool to calculate transmission trains.
	"""
	def __init__(self, mod = 0, teeth = 0, pressure_angle = 20, tilt_angle = 15):
		self.normal_mod = mod
		self.teeth = teeth
		self.pressure_angle = pressure_angle
		self.tilt_angle = tilt_angle
		self.pitch_diameter = self.mod * self.teeth

		self.transversal_mod = self.normal_mod/np.cos(self.tilt_angle)
		self.axial_mod = self.normal_mod/np.sin(self.tilt_angle)

		
		#gear pitch
		self.circular_pitch = self.mod*pi
		self.diametral_pitch = 1/self.mod
		
		#gear geometrical parameters
		self.addendum = self.mod
		self.dedendum = 1.25*self.mod
		self.clearance = self.dedendum - self.addendum
		self.height = self.dedendum + self.addendum
		self.thickness = self.circular_pitch/2
		self.teeth_spacing = self.thickness

		self.width = 13*self.mod
		print("Gear width set to 13*m. Can be changed with the set_width() method by providing a factor betwen 10 and 16")

		#other diameters
		self.head_diameter = self.pitch_diameter + 2*self.mod
		self.base_diameter = self.pitch_diameter*np.cos(pressure_angle)
		self.root_diameter = self.pitch_diameter - 2.5*self.mod

	#width setter
	def set_width(width_factor):
		self.widht = width_factor*self.mod

	#getters
	def get_modulus(self):
		return self.mod

	def get_teeth_number(self):
		return self.teeth

	def get_pitch_diameter(self):
		return self.pitch_diameter

	def get_circular_pitch(self):
		return self.circular_pitch

	def get_diametral_pitch(self):
		return self.diametral_pitch

	def get_addendum(self):
		return self.addendum

	def get_dedendum(self):
		return self.dedendum

	def get_clearance(self):
		return self.clearance

	def get_height(self):
		return self.height

	def get_thickness(self):
		return self.thickness

	def get_teeth_spacing(self):
		return self.teeth_spacing

	def get_width(self):
		return self.width

	def get_head_diameter(self):
		return self.head_diameter

	def get_base_diameter(self):
		return self.base_diameter

	def get_root_diameter(self):
		return self.root_diameter