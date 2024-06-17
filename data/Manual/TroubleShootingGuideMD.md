# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## 4.4 OPERATIVE MANAGAMENT III - OPERATING FAULTS

## 4.4.1 Fault Finding

## 4.4.1.1 PRELIMINARY REMARKS

## 4.4.1.1.1 FAULT-FINDING WITH THE AID OF TABLES 4-24, 4-25 AND 4-

## Tables 4-24, 4-25 and 4-26 contain a selection of possible operating faults and their causes. They are intended

## to contribute to reliable fault diagnosis and rapid resolution of their cause.

## 4.4.1.1.2 CLASSIFICATION

## The faults are grouped into three categories:

## a. Engine start/Engine running,

## b. Operating data and

## c. Other problems.

## Firstly, the possible causes of the faults are not usually limited to a single issue. Quite often several possibilities

## should be considered. The most likely cause can be determined from the points listed, with consideration of

## a. the appearance characteristics,

## b. the time-related and factual aspects and

## c. the person's own experience.

## 4.4.1.1.3 "INFO" AND "CODE" COLUMNS

## The "Info" column contains references to sections in the manual and Work Cards. The "Code" column allows the

## technical service to identify the specific error, so the table can be employed for user questions, such as "What

## happens if...?".

## 4.4.1.1.4 EXAMPLE

## For example, key number 15 appears in the tables in three places (indicated by ●). This means: If the injection

## timing is too far in the direction "late", the following consequences are possible:

## a. the engine does not reach its full power/speed,

## b. the exhaust gas temperatures are too high and

## c. the exhaust gas plumes are visible and have a dark colour.

## 4.4.1.1.5 FAULT FINDING WITH THE TURBOCHARGER

## Please note that the instruction manual for the turbocharger has its own fault-finding in the document

## DO0F466180E.

## Sequence of the entries

## The sequence of the entries has no bearing on the probability of a certain cause. The sequence is based on:

## a. causes related to operating media and their systems,

## b. engine,

## c. turbocharger and

## d. possibly the ship.


# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## 4.4.1.1.6 FAULT FINDING "ENGINE START /RUNNING ENGINE"

```
Table 4-24: Fault finding table
```
## Error/System

## Causes

## INFO

## (Section/Work

## Card in

## DO0F466162E

## Maintenance

## Manual)

## Code

## Crankshaft does not turn when starting. Crankshaft turns too slowly, swings back

```
Compressed air system Pressure in the compressed air tank too low 01
```
(^) Main starting valve faulty 162.xx 02
(^) Starting valve faulty 161.xx 03
(^) Starting air pilot valve faulty 160.xx 05
Control and monitoring system Error in pneumatic or electronic control system 63
Turning gear Switching device not fully disengaged 79

## Engine reaches firing speed, firing does not occur

```
Fuel Fuel quality inadequate 4.1 09
Fuel system Fuel tank empty 06
```
(^) Fuel system not bled 07
(^) Injection pumps fail to pump 3.4, 200.xx 08
Fuel pressure before injection pump too low, feed
pump faulty

### 3.4, 3.5 12

(^) Fuel filter blocked 13
Injection pump/injection pump
drive
Excessiveclearance between injection pumppiston
andpumpcylinder
3.5, 200.xx 16
Speed regulation system Speed governor/booster
faulty/interference/incorrectly adjusted
140.xx 56
(^) Pick-up faulty (engine 32/40) 140.xx, 400.xx 78
Control and monitoring system Filling release missing/too low 65
(^) Error in pneumatic or electronic control system 63

## Cylinders firing irregularly

```
Fuel Fuel quality inadequate 4.1 09
```
(^) Water in fuel 4.1, 000.05 10
Fuel system Fuel system not bled 07
Fuel pressure before injection pump too low, feed
pump faulty

### 3.4, 3.5 12

(^) Fuel filter blocked 13
Injection valve Injection valves faulty 221.xx 20


# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## Error/System

(^)

## Causes

## INFO

## (Section/Work

## Card in

## DO0F466162E

## Maintenance

## Manual)

## Code

```
Inlet and exhaust valves
```
(^) Inlet or exhaust valves are sticking, valve springs
broken, valves leaking
113.xx, 114.xx 26

## The engine does not reach its full power/speed

```
Fuel Fuel quality inadequate 4.1 09
```
(^) Water in fuel 4.1, 000.05 10
(^) Fuel viscosity insufficient, fuel overheated 4.1 66
Fuel system Fuel system not bled 07
Fuel pressure before injection pump too low, feed
pump faulty

### 3.4, 3.5 12

(^) Fuel filter blocked 13
Fuel injection timer
Injection time too late (only for engines with
automatic fuelinjectiontimer)
3.4, 200.xx,
120.xx

### 15 ●

```
Injection pump/injection
drive
```
```
pump Excessiveclearance between injection pumppiston
andpumpcylinder
```
```
3.5, 200.xx 16
```
(^) Injection pump plunger sticking, spring broken 200.xx 17
Control rod, regulating sleeve or pump element
sticking
200.xx 18
Leaky pressure valve in the injection pump 200.xx 19
Injection valves
Injection valves faulty 221.xx 20
Nozzle openings or injection pipes blocked 221.xx 21
Speed governor/ Control linkage Speed governor/booster 140.xx 56
faulty/interference/incorrectly adjusted
Governor or control linkage misadjusted 3.4, 140.xx 22
Governor control linkage stiff or jammed 203.xx 23
Inlet and exhaust valves
Inlet or exhaust valves are sticking, valve springs
broken, valves leaking
113.xx, 114.xx 26
Control and monitoring system Filling release missing/too low 65
Speed release too low
89
Turbocharger
Turbocharger contaminated or faulty 500.xx 49


# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## Error/System

(^)

## Causes

## INFO

## (Section/Work

## Card in

## DO0F466162E

## Maintenance

## Manual)

## Code

```
Ship
formarineengines:Propellerdamagedorfoulingon
the ship's hull
```
### 45

## Engine running unevenly, knocking

```
Fuel system Fuel system not bled 07
```
```
Fuel pressure before injection pump too low, feed
pump faulty
```
### 3.4, 3.5 12

(^) Fuel filter blocked 13
Engine Engine or individual cylinders severely overloaded 3.5, 4.3 25
Fuel injection timer
Injection time too early (only for engines with
automatic fuelinjectiontimer)
3.4, 200.xx,
120.xx

### 14

```
Injection pump/injection
drive
```
```
pump Injection pump plunger sticking, spring broken 200.xx 17
```
```
Injection valves Injection valves faulty 221.xx 20
```
```
Inlet and exhaust valves
```
(^) Inlet or exhaust valves are sticking, valve springs
broken, valves leaking
113.xx, 114.xx 26
(^) Excessive valve clearance 111.xx 90

## Engine running at fluctuating speeds

```
Fuel Air in fuel 75
```
```
Fuel system
```
(^) Fuel pressure before injection pump too low, feed
pump faulty

### 3.4, 3.5 12

```
Speed governor/ Control linkage Governor misadjusted, control linkage overly 3.4, 140.xx 22
extended
```
```
Speed governor/booster
faulty/interference/incorrectly adjusted
```
```
140.xx 56
```
(^) Governor control linkage stiff or jammed 203.xx 23
Pick-up faulty (engine 32/40) 140.xx, 400.xx 78
Injection pump/injection
drive
pump Control rod, regulating sleeve or pump element
sticking
200.xx 18
Control and monitoring system Speedreferencevalue unstable(airleakage/electrical 58
signal)

## Engine speed drops, engine stops


# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## Error/System

## Causes

## INFO

## (Section/Work

## Card in

## DO0F466162E

## Maintenance

## Manual)

## Code

```
Fuel Water in fuel 4.1, 000.05 10
Fuel system Fuel tank empty 06
```
```
Fuel pressure before injection pump too low, feed
pump faulty
```
### 3.4, 3.5 12

(^) Fuel filter blocked 13
Engine Engine or individual cylinders severely overloaded 3.5, 4.3 25
Speed governor/ Control linkage Set speed value failed
59
(^) Governor control linkage stiff or jammed 203.xx 23
Control and monitoring system Shut-down device triggered 3.4 24

## Overspeed protection triggered

```
Speed governor/ Control linkage Speed governor/booster
faulty/interference/incorrectly adjusted
```
```
140.xx 56
```
(^) Speed governor - Setting of the "dynamics" 140.xx 57
(^) Governor control linkage stiff or jammed 203.xx 23
Control and monitoring system Overspeed relay faulty 85

## Exhaust gas plume sooty, dark

```
Fuel Fuel quality inadequate 4.1 09
Engine Engine or individual cylinders severely overloaded 3.5, 4.3 25
Charge air system Charge air too cold 3.5 73
```
```
Fuel injection timer Injection time too late (only for engines with
automatic fuelinjectiontimer)
```
```
3.4, 200.xx, 15 ●
```
```
Injection pump/injection pump
drive
```
```
Fuel injection pump, baffle screws worn 200.xx 69
```
```
Injection valves Injection valves faulty 221.xx 20
```
```
Inlet and exhaust valves Inlet or exhaust valves are sticking, valve springs
bro- ken, valves leaking
```
```
113.xx, 114.xx 26
```
```
Control and monitoring system Charge limit too high (marine main engines - only in
manoeuvring operation)
```
(^64)
Turbocharger Turbocharger contaminated or faulty 500.xx 49
(^) Air intake filter clogged (lack of air) 91

## Exhaust gas plume bluish

```
Fuel Water in fuel 4.1, 000.05 10
```

# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## Error/System

(^)

## Causes

## INFO

## (Section/Work

## Card in

## DO0F466162E

## Maintenance

## Manual)

## Code

```
Lube oil system Oil level in oil sump too high (wet sump) 34
Piston/Piston rings Excessive piston ring clearance or gap too big 3.5, 034.xx 28
```
(^) Piston rings stuck fast or broken 034.xx 32
Turbocharger
Turbocharger over-lubricated 500.xx 92

## Noise from valve or injection pump drive (noise speed-related)

```
Injection pump/injection
drive
```
```
pump Injection pump plunger sticking, spring broken 200.xx 17
```
```
Drive roller faulty or broken spring 200.xx 46
```
```
Inlet and exhaust valves
```
(^) Inlet or exhaust valves are sticking, valve springs
bro- ken, valves leaking
113.xx, 114.xx 26
(^) Excessive valve clearance 111.xx 90

## Fumes from crankcase/crankcase ventilation, muffled noises originating from crankcase

```
Lubricating oil Water content too high 4.1, 000.05 81
Engine Crankcase ventilation blocked 93
```
```
Piston/Piston rings
Excessive piston ring clearance or gap too big 034.xx 32
```
```
Running gear/Crankshaft
Piston or bearing running hot or starting to pick up 3.4, 4.3 31
```
## Oil mist detector triggered

```
Oil mist detector Sensitivity incorrectly set 76
```
```
Condensed water in measuring unit(if engine-room
fansblowcoldairontodetector)
```
### 77

```
Lubricating oil Lubricating oil - water content too high 4.1, 000.05 81
```
```
Piston/Piston rings
Excessive piston ring clearance or gap too big 3.5, 034.xx 28
```

# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## Error/System

## Causes

## INFO

## (Section/Work

## Card in

## DO0F466162E

## Maintenance

## Manual)

## Code

```
Running gear/Crankshaft Piston or bearing running hot or starting to pick up 3.4, 4.3 31
```
## Splash oil monitoring system triggered

```
Lubricating oil Lubricating oil - Temperature too high 104
```
```
Lubricating oil - Temperature deviation from the
mean value too great
```
### 105

```
Running gear/Crankshaft Piston or bearing running hot or starting to pick up 3.4, 4.3 31
```

# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## 4.4.1.1.7 FAULT FINDING "OPERATING DATA"

```
Table 4-25: Errors and their causes/fault finding – Part 2 – "Operating Data"
```
## Error/System

## Causes

## INFO

## (Section/Work

## Card in

## DO0F466162E

## Maintenance

## Manual)

## Code

## Cooling water temperature too high

```
Cooling water system (HT system) Cooling water shortage or air in the cooling
watersystem
```
### 42

(^) Cooling water chambers and/or radiator 000.08 43
(^) Cooling water pump faulty 44
(^) Temperature control faulty 47
(^) Preheating device active 87
Engine Engine or individual cylinders severely 3.5, 4.3 25
Control and monitoring system Indicating instrument or connection line faulty
39

## Cooling water pressure too low

```
Cooling water system (HT system) Cooling water level in the tank too low
70
```
(^) Leakage in the system 71
(^) Lines blocked, components blocked 74
(^) Cooling water pump faulty 44
(^) Stand-by pump not started 82
Control and monitoring system Indicating instrument or connection line faulty 39
(^) Pressure switch/Measuring transducer faulty 61

## Lube oil temperature too high

```
Cooling water system (re-cooling
system)
```
```
Cooling water shortage or air in the cooling
watersystem
```
### 42

(^) Cooling water chambers and/or radiator
contaminated

### 000.08 43

(^) Cooling water pump faulty 44
(^) Temperature control faulty 47
(^) Preheating device active 87
Control and monitoring system Indicating instrument or connection line faulty 39

## Lube oil pressure too low


# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## Error/System

## Causes

## INFO

## (Section/Work

## Card in

## DO0F466162E

## Maintenance

## Manual)

## Code

```
Lube oil system Low oil level in the service tank 35
```
```
Pressure relief valve of the lube oil pump,
broken spring
```
### 36

(^) Pressure regulating valve faulty 60
(^) Lube oil pipes leaking 37
(^) Lube oil lines blocked 80
(^) Lube oil filter clogged 38
(^) Lube oil pump faulty 41
Stand-by pump not started
82
Control and monitoring system Indicating instrument or connection line faulty
39

## Exhaust gas temperature (level control deviation or mean value change)

```
Fuel system Fuel pressure before injection pump too low,
feed pump faulty
```
### 3.4, 3.5 12

```
Engine Engine or individual cylinders severely 3.5, 4.3 25
```
```
Charge air system Charge air temperature too high, charge air
pressure toolow
```
### 3.5 48

(^) Error in the bypass system 62
Injection time maladjustment Injection time too late (only for engines with
automatic fuelinjectiontimer)
3.4, 200.xx,
120.xx

### 15 ●

```
Injection valves Injection valves faulty 221.xx 20
Fuel injection pump Fuel injection pump - incorrect setting 200.xx 67
```
(^) Fuel injection pump faulty 200.xx 68
Cylinder head Cylinder head - Inlet duct contaminated 055.xx 88
Inlet and exhaust valves Inlet or exhaust valves are sticking, valve
springsbroken, valves leaking
113.xx, 114.xx 26
Control and monitoring system Indicating instrument or connection line faulty 39
(^) Temperature sensor faulty 84
(^) Cabling/Connections defective/faulty 86
Turbocharger Turbocharger contaminated or faulty 500.xx 49
Ship for marine engines: Propeller damaged or
foulingon theship's hull

### 45

## Charge air temperature too high


# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## Error/System

## Causes

## INFO

## (Section/Work

## Card in

## DO0F466162E

## Maintenance

## Manual)

## Code

```
Intake air system/ Charge air system Intake temperature too high 3.5 50
```
```
Charge air cooler contaminated (pressure
difference too great)
```
```
3.5, 322.xx 53
```
(^) Leakage on air and exhaust side 52
Exhaust gas system Exhaust gas counter pressure too high
(exhaust boiler contaminated)

### 3.5 54

```
Injection time maladjustment Injection time too early (only for engines with
automatic fuelinjectiontimer)
```
```
3.4, 200.xx, 14
```
```
Control and monitoring system Indicating instrument or connection line faulty
39
```
```
Turbocharger Air filter, compressor/turbine side of the
turbocharger contaminated /damaged
```
```
500.xx 51
```
## Charge air pressure too low

```
Intake air system/ Charge air system Intake temperature too high 3.5 50
```
(^) Charge air cooler contaminated (pressure
difference too great)
3.5, 322.xx 53
(^) Leakage on air and exhaust side 52
Exhaust gas system Exhaust gas counter pressure too high
(exhaust boiler contaminated)

### 3.5 54

```
Injection time maladjustment Injection time too early (only for engines with
automatic fuelinjectiontimer)
```
```
3.4, 200.xx, 14
```
```
Control and monitoring system Indicating instrument or connection line faulty
39
```
```
Turbocharger Air filter, compressor/turbine side of the
turbocharger contaminated /damaged
```
```
500.xx 51
```
## Crankshaft bearing - temperature too high

```
Crankshaft bearing Bearing damaged, faulty lubrication 021.xx 72
Engine Alignment/foundation faulty 000.09, 012.xx 95
Control and monitoring system Temperature sensor faulty 84
```
(^) Cabling/Connections defective/faulty 86


# OPERATING FAULTS (TROUBLE SHOOTING )

## PROJECT:

## VERSION: SECTION:

## 4.4.1.1.8 FAULT FINDING- OTHER PROBLEMS

```
Table 4-26: Errors and their causes/Fault finding – Part 3 – "Other Problems"
```
## Error/System

## Causes

## INFO

## (Section/Work

## Card in

## DO0F466162E

## Maintenance

## Manual)

## Code

## Stiff/blocked movement of the governor control linkage of the injection pumps

```
Speed governor/ Control linkage Governor or control linkage misadjusted 3.4, 140.xx 22
```
```
Governor control linkage stiff or jammed 203.xx 23
Control and monitoring system Shut-down device triggered 3.4 24
```
## Injection pump delivers unevenly

```
Fuel Fuel viscosity insufficient, fuel overheated 4.1 66
Fuel system Fuel system not bled 07
```
```
Fuel too cold, solidified in the fuel pipes
(heavy fuel)
```
### 4.1 11

(^) Fuel pressure before injection pump too low,
feed pump faulty

### 3.4, 3.5 12

(^) Fuel filter blocked 13
Injection pump/ injection pump drive Injection pump plunger sticking, spring
broken
200.xx 17
(^) Leaky pressure valve in the injection pump 200.xx 19
Controlrod,regulatingsleeveorpump
elementsticking
200.xx 18

## Starting pipe to cylinder head getting hot

```
Cylinder head Starting valve leaky 161.xx 04
```
## Safety valve in the cylinder head blows off

```
Engine Engine or individual cylinders severely 3.5, 4.3 25
Cylinder head Safety valve, spring broken 057.xx 27
Injection time maladjustment Injection time too early (only for engines with
automatic fuel injection timer)
```
```
3.4, 200.xx, 120.xx 14
```

