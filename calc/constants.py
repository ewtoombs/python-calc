# The canonical constants of science, with an emphasis on physics.

tau = 6.283185307179586
sqrttau = 2.5066282746310002
sqrt1_tau = 0.3989422804014327
sqrt2 = 1.4142135623730951
sqrt1_2 = 0.7071067811865476
sqrt3 = 1.7320508075688772

# To keep things clear, in this context, the noun "quantity" will be used to
# refer to a real number with dimension. Examples are 5 kg and 400 nm. A unit
# is a standard quantity used to express other quantities. An quantity
# expressed in terms of a dimensionless real number multiplied by a standard
# unit shall be provisionally called a "translation".  It has two parts: the
# dimensionless real number and the unit, which shall be provisionally called
# the "word".  For example, 5000 g and 5 kg are translations of the same
# quantity. For 5000 g, 5000 is the word and g is the unit. A physical constant
# like hb is an quantity with many translations, depending on the conventions
# of the field.  (The inspiration for the new terms is that the same object may
# be referred to in different languages with different words.  Each (word,
# language) pair is a translation of the same object.  In this context, the
# unit is like the language.)

# Ultimately, all quantities must be stored in a machine as just a word, with
# some kind of implied unit (and translation). A "machine unit" (and machine
# translation) is the unit that is implied by default.  For example, right now
# metre is a machine unit, so all lengths are stored in metres by default.  The
# machine units for physical quantities in this context are the SI base and
# derived units: s, kg, m, K for the base units and A, N, J, W, Pa, Ohm, etc.
# for the derived units.

# A variable for each of the machine units has been made. Each is equal to 1.
# These are more for documentation than anything, so that you can define
# quantities in your code like this: t = 40*second and it is completely
# clear that t is a time and the time is 40 seconds. But if for whatever
# reason, second ceases to be a base unit (for instance in a relativity
# context, time is often measured in metres), no change to the code will be
# necessary.
second = 1.0
# My solution to the awkward presence of kilo in the base unit, which was 
# always a stupid idea.
grave = 1.0
kilogram = grave
# The ton is generally useful, but particularly for use with the volumetric 
# prefixes below, since 1*ton lines up with 1*metre**3 in order of magnitude.  
# (1 metre**3 of water .= 1 ton)
ton = 1000*kilogram
metre = 1.0
kelvin = 1.0
ampere = 1.0

# For data, the machine unit is bits. For this one, integers are often
# sensible, so I do not force floating point with a .0 at the end.
bit = 1

# For angle, the machine unit is radians.
radian = 1.0

# Some derived machine units. They are not set to 1 in case fiddling with the
# base machine units is necessary. For instance, in quantum mechanics
# simulations, it can be useful to set hb to 1, removing kg as a base unit (and
# as a machine unit).  grave will no longer equal 1, so any units here that
# rely on it will change as well.
newton = grave*metre/second**2
pascal = newton/metre**2
joule = newton*metre
watt = joule/second
coulomb = ampere*second
volt = joule/coulomb
tesla = newton/ampere/metre
ohm = volt/ampere
farad = coulomb/volt

# The SI prefixes. Using these is straight forward. Example: 1km = 
# 1*kilo*metre.
yotta = 1e24
zetta = 1e21
exa = 1e18
peta = 1e15
tera = 1e12
giga = 1e9
mega = 1e6
kilo = 1e3

milli = 1e-3
micro = 1e-6
nano = 1e-9
pico = 1e-12
femto = 1e-15
atto = 1e-18
zepto = 1e-21
yocto = 1e-24

# Volumetric SI prefixes. My own invention. Use them for quantities Q that
# scale cubically with the length scale to keep Q in the same prefix as length.
# For example, the Earth is roughly 10 Mm in diameter and weighs about 5000
# mevatons. Its volume is about 1000 Mm^3. From here, you can use the numbers
# directly, since the meva cancels the mega cubed. 5000 mevatons/1000Mm^3 = 5
# tons/m^3, or five times denser than water. You couldn't do that with the
# regular scale.  You would break the bank, since there isn't even a prefix big
# enough, though you could write 5 000 yottagraves.  Yotta doesn't match with
# mega, but meva does.
yova = 1e72
zeva = 1e63
eva = 1e54
peva = 1e45
teva = 1e36
giva = 1e27
meva = 1e18
kivo = 1e9

mivi = 1e-9
micvo = 1e-18
navo = 1e-27
pivo = 1e-36
femvo = 1e-45
avo = 1e-54
zepvo = 1e-63
yocvo = 1e-72

# Surface area SI prefixes. Same idea. They can even be used on mass when the
# mass is covering a surface, and so, varies by area instead of by volume.
yosa = 1e48
zesa = 1e42
esa = 1e36
pesa = 1e30
tesa = 1e24
gisa = 1e18
mesa = 1e12
kiso = 1e6

misi = 1e-6
micso = 1e-12
naso = 1e-18
piso = 1e-24
femso = 1e-30
aso = 1e-36
zepso = 1e-42
yocso = 1e-48

# Dealing with non-machine units and translations: All quantities are always 
# stored in the machine translation in this context, so to store a non-machine 
# translation, conversion is done immediately. Since all units are quantities, 
# non-machine units are treated as such when represented in this context, i.e.  
# they are given a variable name and stored in the base units.  The form for 
# storing non-machine translations is thus quantity = word*unit.  For example, 
# height= 6*inch or theta = 90*deg.  Thus conversion of a stored quantity to a 
# non-machine translation (for the purpose of display usually) will look like 
# this: quantity/unit.  It is read "quantity in units". For example, 
# height/inch is "height in inches".  Consequently, conversion to and from 
# non-machine translations looks like this: word*unit1/unit2.  It is read 
# "word unit1s in unit2s". For example, 100*inch/foot is "100 inches in feet".

# These are the non-machine units:

# data
byte = 8*bit
KB = 1024*byte
MB = 1024*KB
GB = 1024*MB
sector = 512*byte

# the degree
deg = tau/360*radian

# The gram in graves. Handy for expressions like micro*gram.
gram = milli*grave
# the litre. Not a machine unit. This was to make volume math like V = 2*tau/3
# * r**3 easier. A machine unit of one litre would make a total mess of that
# formula. Like any non-machine unit, if you want litres, do a conversion at
# the point of need like foreign_function_requires_litres(V/litre) or
# print('{}L'.format(V/litre)). A foreign function that returns litres should
# be handled like V = somebody_elses_volume()*litre.
litre = metre**3/1000
# The angstrom
angstrom = 100*pico*metre


# Standard gravitational acceleration. Though technically a physical constant, 
# it is exact for units like poundf, but average for the actual acceleration 
# due to gravity, which varies from place to place.
g = 9.80665*metre/second**2


# The horrible units. All quantities here are exact, and derived from SI 
# units. I only cover the reasonably common ones. I don't do any of the REALLY 
# obscure shit like rods or grains or slugs or whatever.

# mass
pound = 453.59237*gram  # exact, from SI
ounce = pound/16

# length
inch = 25.4*milli*metre  # exact, from SI
foot = 12*inch
mile = 5280*foot

# area
acre = 4046.8564224  # the international acre

# volume (The machine unit is one cubic metre. This machine unit was
# chosen to simplify precisely the kind of calculations that follow here. See
# the litre above for more.)
gallon = 231*inch**3
floz = gallon/128
#quart = gallon/4
#pint = gallon/8
# One Apple gallon. No, just kidding. It's one imperial gallon, i.e. Great 
# Britain's gallon.  It is defined exactly from litres these days, so this is 
# also an entry point from SI. Defined to the nearest 10*micro*litre.
igallon = 4.54609*litre  # exact, from SI
# This one is included in honour of one of the most common ways of buying 
# liquour in Canada *to this day*: The imperial quart. (approximitely 1.14 L.  
# Sound familiar?)
iquart = igallon/4
ifloz = igallon/160

# some others.
# Pound force in newtons
poundf = pound*g
# Pounds per square inch, in pascals. The unit is named ppsi so psi can be 
# used as a Greek letter.
ppsi = poundf/inch**2

# Time, the most horrible unit of them all.
minute = 60*second
hour = 60*minute
day = 24*hour
week = 7*day
# Julian year, since the real thing is so fickle.
year = 365.25*day
# A typical month, as 1/12 of a Julian year.
month = year/12


# Physical Constants
# ==================
# Planck's constant.
hb = 1.05457162853e-34*joule*second
# Non-reduced Planck's constant. Just h is too assertive over the namespace.  
# Ideally, this whole file could be imported without a prefix, i.e. from 
# constants import *
hnr = tau*hb
kb = 1.3806505e-23*joule/kelvin
NA = 6.0221415e23
mole = NA
amu = gram/NA

G = 6.67384e-11*newton*metre**2/grave**2

# Ideal gas constant
RG = NA*kb

# Bohr radius
a0 = 5.2917721092e-11*metre

# This one is exact and defines the metre from the second.
c0 = 299792458*metre/second
# This only works for the word "light" used in measures of distance---not time.
# But hardly anybody ever uses expressions like "light metres", even though
# they could. So, this is basically fine. Example: a lightyear is simply
# light*year.
light = c0
mu0 = tau*2e-7*newton/ampere**2
ep0 = 1/(mu0*c0**2)
kc = 1/(2*tau*ep0)  # Coulomb's constant


me = 9.10938291e-31*grave     # mass of an electron
mp = 1.672621777e-27*grave    # mass of a proton
qe = 1.602176565e-19*coulomb     # fundamental charge

# The electron volt.
eV = qe*volt

# equatorial radius of Earth
rE = 6.3710*mega*metre
# mass of Earth
mE = 5.97219e24*grave

au = 149.597870700*giga*metre  # exact
