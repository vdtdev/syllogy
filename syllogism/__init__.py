#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Logic -> Syllogisms
#  
#  Copyright 2013 Wade Harkins <vdtdev@gmail.com>
#  
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are
#  met:
#  
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above
#    copyright notice, this list of conditions and the following disclaimer
#    in the documentation and/or other materials provided with the
#    distribution.
#  * Neither the name of the  nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#  
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
#  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
#  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
#  A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
#  OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
#  SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
#  LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
#  DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
#  THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
#  (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
#  OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
	
	""" Forms a sentence from the terms and specified form """
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
	
	""" Returns a 3 character mood type """
	def mood(self):
		return self._maj.form.name + self._min.form.name + self._con.form.name

	""" Prints out a standard form syllogism """
	def formal(self):
		print self._maj.sentence()
		print self._min.sentence()
		print "------------------------"
		print self._con.sentence()
		
	""" Determins the figure of the syllogism"""
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
				
			
