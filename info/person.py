class Person:

  def __init__(self, 
  			   firstName, 
  			   lastName,
  			   birthDay,
  			   birthMonth,
  			   birthYear):

    self.firstName   = firstName
    self.lastName    = lastName
    self.birthDay	 = int(float(birthDay))
    self.birthMonth  = int(float(birthMonth))
    self.birthYear   = int(float(birthYear))

  def getFirstName(self):
  	return self.firstName

  def setFirstName(self,firstName):
  	self.firstName = firstName

  def getLastName(self):
  	return self.lastName

  def setLastName(self,lastName):
  	self.lastName = lastName


  def __str__(self):
        return self.firstName + " " + self.lastName + " {0}/{1}/{2}".format(self.birthMonth,self.birthDay,self.birthYear)

