#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Logic -> Syllogisms
#  
#  Copyright 2013 Wade Harkins <vdtdev@gmail.com>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

# Represents the form of a syllogism predicate statement
class Form:
	"""
	Predicate form constructor
		universal: Predicate is universal
		affirmative: Predicate is affirmative
	"""
	def __init__(self,universal,affirmative):
		self._universal_=universal
		self._affirmative_=affirmative
		if self._universal_:
			if self._affirmative_:
				self._name_="A"
			else:
				self._name_="E"
		else:
			if self._affirmative_:
				self._name_="I"
			else:
				self._name_="O"		
	
	def __set_name__(self,name):
		self._name_=name
	
	def __get_name__(self):
		return self._name_

	def __get_universal__(self):
		return self._universal_

	def __get_affirmative__(self):
		return self._affirmative_
	
	affirmative = property(__get_affirmative__,None,"Is form affirmative")
	universal = property(__get_affirmative__,None,"Is form affirmative")
	name = property(__get_name__,__set_name__,None,"Form name")
	

""" Form lookup dictionary """
formDict = dict()
formDict["A"]=Form(True,True)
formDict["E"]=Form(True,False)
formDict["I"]=Form(False,True)
formDict["O"]=Form(False,False)


class Terms:
	
	def __init__(self,subject,predicate):
		self._subject=subject
		self._predicate=predicate
	
	def __get_predicate__(self):
		return self._predicate
	
	def __get_subject__(self):
		return self._subject
	
	predicate=property(__get_predicate__,None,None,"Predicate term")
	subject=property(__get_subject__,None,None,"Subject")

class Statement:
	
	def __init__(self,terms,form):
		self._terms=terms
		self._form=form
	
	def __get_terms__(self):
		return self._terms
	
	def __get_form__(self):
		return self._form
	
	terms = property(__get_terms__,None,None,"Terms")
	form = property(__get_form__,None,None,"Form")
	
	def sentence(self):
		quant = ""
		copula = ""
		if self._form.universal:
			copula="are"
			if self._form.affirmative:
				quant="All"
			else:
				quant="No"
		else:
			quant="Some"
			if self._form.affirmative:
				copula="are"
			else:
				copula ="are not"
		
		return quant + " " + self._terms.subject + " " + copula + " " + self._terms.predicate

"""
Encapulsation of a full categorical syllogism
"""
class Syllogism:
	
	def __init__(self,major,minor,conclusion):
		self._maj=major
		self._min=minor
		self._con=conclusion
	
	def __get_major__(self):
		return self._maj
	def __get_minor__(self):
		return self._min
	def __get_conclusion__(self):
		return self._con
	
	major = property(__get_major__,None,None,"Major premise")
	minor = property(__get_minor__,None,None,"Minor premise")
	conclusion = property(__get_conclusion__,None,None,"Conclusion")
	
	def mood(self):
		return self._maj.form.name + self._min.form.name + self._con.form.name

	def formal(self):
		print self._maj.sentence()
		print self._min.sentence()
		print "------------------------"
		print self._con.sentence()
		
	def figure(self):
		s = self._con.terms.subject
		p = self._con.terms.predicate
		if self.major.terms.predicate == p:
			if self.minor.terms.subject == s:
				return 1
			if self.minor.terms.predicate == s:
				return 3
		else:
			if self.minor.terms.subject == s:
				return 2
			if self.minor.terms.predicate == s:
				return 4
		return 0
				
			
