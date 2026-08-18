# Engineering Principles

This appendix covers the foundational aerospace and engineering theories applied in the Pilot Kit projects.

## 1.1 Paper Dart Glider

**The Four Forces of Flight**

Every aircraft in flight is acted upon by four forces. Understanding how these interact is the foundation of aeronautical engineering.

| **Force** | **Direction** | **Explanation** |
| --- | --- | --- |
| **Lift** | Upward force | Created by wing shape and angle of attack |
| **Drag** | Rearward force | Air resistance that slows the aircraft |
| **Weight** | Downward force | Gravity acting on the aircraft mass |
| **Thrust** | Forward force | Provided by the human launch (hand) |

**Design Features That Affect Flight**

* Wing Area – Larger wings generate more lift but also more drag, reducing speed
* Aspect Ratio – Long, narrow wings (high aspect ratio) produce a better glide ratio than short, wide wings
* Centre of Gravity (CG) – The CG must be slightly forward of the aerodynamic centre for stable flight
* Symmetry – Any asymmetry in the wing or fuselage will cause the aircraft to turn during flight
* Surface Smoothness – Rough or crumpled surfaces increase drag and reduce flight distance

**Bernoulli's Principle (Simplified)**

| **Key Concept**  When air flows over a curved surface, it must travel farther – and therefore faster – than air flowing under a flat surface.  Faster-moving air exerts lower pressure (Bernoulli's Principle).  The higher pressure beneath the wing pushes upward, creating LIFT. |
| --- |

---

## 1.10 Balsa Wood Tower

**Structural Concepts**

* Compression: forces pushing inward along a column. Columns under compression are prone to buckling if they are slender
* Tension: forces pulling outward along a member. Diagonal braces usually carry tension when a column is pushed
* Buckling: sudden sideways collapse of a slender column under compression. The most common failure mode in balsa towers
* Triangulation: dividing a rectangular panel into triangles makes it rigid — a triangle cannot change shape without changing its member lengths
* Efficiency: the ratio of load carried to structure weight is the most important metric in aerospace structural design

| **Aviation Connection**  Aircraft wings use a spar as the main compression/tension member, with ribs providing shape and preventing buckling.  The Eiffel Tower (also a structural landmark in aviation history) uses the same X-bracing principle students test in this project.  Modern composite aircraft fuselages are designed to achieve structural efficiency ratios far exceeding any metal design — exactly the metric students calculate here. |
| --- |

---

## 1.11 Straw Paper

**Airframe Structural Members**

* Spar: the main spanwise structural member of the wing; carries bending loads from lift
* Rib: cross-sectional members perpendicular to the spar; give the wing its shape and transfer loads to the spar
* Fuselage: the main body structure; must carry the weight of passengers, cargo, engines, and fuel — all transferred to the wings
* Stringer: longitudinal members running along the fuselage length; resist bending and compression

| **Load Path in a Real Wing**  Lift is generated across the entire wing surface and acts perpendicular to the airflow.  This distributed lift force is collected by the wing ribs and transferred to the main spar.  The spar carries it inboard to the wing root, where it is transferred into the fuselage structure.  The fuselage distributes the load through its frames and stringers to the landing gear and tail.  If any element in this chain fails, the aircraft is lost — load path integrity is non-negotiable. |
| --- |

---

## 1.12 Kite Building

**Kite Aerodynamics**

* Lift: the kite's angled surface deflects wind downward, creating an upward reaction force (Newton's Third Law) — this is lift
* Drag: the kite also resists the wind, creating drag that pulls it back and holds it at an angle
* Tension: the flying string holds the kite at the bridle angle, balancing lift and drag
* Bridle angle: the point where the string attaches determines the kite's angle of attack; moving it higher flattens the angle and reduces lift
* Stability: the tail acts as a pendulum moment — wind force on the tail creates a restoring torque that prevents spinning

| **Aviation Historical Connection**  Lawrence Hargrave invented the box kite in 1893 — the same structural principle was used in the wings of early biplanes.  Samuel Langley and Octave Chanute used kite experiments to study lift long before the Wright Brothers' first flight.  The Wright Brothers used a kite with control surfaces to test wing warping — the concept that became the aileron — before they built their first glider.  Modern power kites (kitesurfing, kite buggies) generate hundreds of kilograms of lift — all from the same principles in this project. |
| --- |

---

## 1.13 Airfoil Shape Comparison

* Bernoulli's Principle: a cambered airfoil forces air to travel farther over its curved top surface, so it must travel faster; faster flow = lower pressure; lower pressure above = lift
* Angle of attack: the angle between the chord line and the oncoming airflow; increasing AoA increases lift up to the stall angle
* Stall: above the critical angle of attack, airflow cannot follow the upper surface; it separates; pressure equalises; lift drops suddenly
* Under-cambered airfoils: popular on slow-flying model aircraft and kites — high lift at low speeds; poor at higher speeds due to drag

|  |
| --- |
| **Real Wind Tunnel Connection**  Every aircraft airfoil in the world has been tested in a wind tunnel before being certified for flight.  The data students collect in this project is structurally identical to wind tunnel data: lift coefficient vs. angle of attack.  The Airbus A380 wing profile was tested at subsonic, transonic, and supersonic speeds before the aircraft was built.  Students are conducting the same class of experiment using a desk fan instead of a million-dollar facility. |

---

## 1.14 Propeller Thrust

* Thrust: force generated by the propeller accelerating a mass of air rearward; Newton's Third Law — equal and opposite reaction pushes the aircraft forward
* Diameter: larger diameter propellers move more air per revolution, generating more thrust at the same RPM but requiring more torque from the motor
* Pitch: the angle of the propeller blade; high pitch moves more air per revolution but needs more power; low pitch needs less power but produces less thrust
* Efficiency: the ratio of useful thrust to electrical power consumed. A large, slow-spinning propeller is more efficient than a small, fast-spinning one — why all long-endurance aircraft use large propellers

|  |
| --- |
| **Real Aviation Connection**  This rig is a simplified version of the thrust test benches used by propeller manufacturers.  Every propeller fitted to a certified aircraft must pass a documented thrust and efficiency test.  The most efficient propellers on earth are on long-endurance UAVs like the AeroVironment Global Observer — 2-metre span blades turning at 300 RPM, designed using exactly the principles measured in this project. |

---

## 1.2 Foam Hand Launch

**Airfoil Shape & Lift Generation**

An airfoil is a shape designed to generate lift when moving through air. The curved upper surface of the wing forces air to travel a longer path than the air moving under the flat lower surface. By Bernoulli's Principle, faster-moving air exerts lower pressure — creating a net upward force (lift) on the wing.

| **Key Formula**  Lift (L) = CL x (1/2 x rho x V^2) x A  Where: CL = lift coefficient (wing shape), rho = air density, V = speed, A = wing area  Practical implication: doubling the speed quadruples the lift produced. |
| --- |

**Centre of Gravity & Aerodynamic Centre**

* The Centre of Gravity (CG) is the point at which the aircraft's total weight acts downward
* The Aerodynamic Centre (AC) is the point at which the total lift force acts — approximately 1/4 chord from the leading edge for most wings
* For stable flight, CG must be slightly forward of AC
* If CG moves behind AC, the aircraft becomes unstable and tends to pitch nose-up, leading to a stall

**Stability Types**

| **Stability Type** | **Behaviour** | **Design Factor** |
| --- | --- | --- |
| **Static Stability** | Returns to level after a disturbance | CG forward of aerodynamic centre |
| **Dynamic Stability** | Oscillations dampen over time | Dihedral angle and tail size |
| **Neutral Stability** | Holds new attitude after disturbance | CG at aerodynamic centre |
| **Instability** | Diverges further from level | CG behind aerodynamic centre |

**Flight Control Surfaces**

Control surfaces are small movable sections of the wing and tail that change the direction of airflow, producing forces that rotate the aircraft about its three axes.

| **Surface** | **Location** | **Controls** | **How to Adjust** |
| --- | --- | --- | --- |
| **Elevator** | Horizontal stabilizer | Pitch (nose up / nose down) | Bend trailing edge up/down |
| **Rudder** | Vertical stabilizer | Yaw (nose left / nose right) | Bend trailing edge left/right |
| **Ailerons** | Outer wing trailing edge | Roll (bank left / bank right) | Bend opposite sides up/down |

**Dihedral Effect**

| **Dihedral Explained**  Dihedral is the upward angle of the wings when viewed from the front.  When a gust rolls the aircraft, the lower wing presents a greater angle of attack and generates more lift, automatically returning the aircraft to level flight.  Our foam glider uses a small dihedral angle (5–10 degrees) built into the wing template for this reason. |
| --- |

---

## 1.3 Rubber Band Powered

**Energy Conversion Chain**

The rubber-band motor is a complete energy system. Every flight demonstrates a chain of energy conversions from start to finish.

| **Energy Form** | **Where In System** | **Key Fact** |
| --- | --- | --- |
| **Stored (Elastic Potential)** | Wound rubber band | Energy increases with turns squared |
| **Kinetic (Rotating)** | Spinning propeller shaft | Converted from stored energy as band unwinds |
| **Kinetic (Thrust)** | Air pushed rearward | Newton's 3rd Law: aircraft pushed forward |
| **Lost (Heat & Friction)** | Hook bearings, air drag | Reduces with smoother bearings and less excess glue |

**Newton's Third Law & Propeller Thrust**

| **Key Principle**  The propeller pushes a column of air backward (action).  The air pushes the aircraft forward with an equal and opposite force (reaction) — this is THRUST.  Propeller efficiency depends on three factors: pitch (angle of the blade), diameter, and rotational speed.  An over-wound rubber band spins the propeller too fast, causing the blades to slip through the air like a car wheel spinning on ice — this is why performance peaks and then falls. |
| --- |

**Diminishing Returns — Why More Turns Doesn't Always Mean More Flight**

* Below the optimum: more turns = more stored energy = longer flight
* At the optimum: the rubber band is fully loaded within its elastic range — maximum efficiency
* Beyond the optimum: the rubber band stretches past its elastic limit; energy is lost as heat; propeller over-speeds and stalls the air column
* Real aircraft face the same principle: jet engines have a maximum efficient throttle setting beyond which fuel burn rises faster than thrust

---

## 1.4 Rc Flight Simulator

**RC Control System – How It Works**

A radio control system converts physical stick movements on the transmitter into electronic signals, which are received by a receiver on the aircraft and converted into servo movements that deflect the control surfaces. In a simulator, this chain is replicated digitally — the transmitter output feeds directly into the simulator's physics engine.

**The Four Controls – Reference Table**

| **Control** | **Stick / Axis** | **Effect** | **Key Note** |
| --- | --- | --- | --- |
| **Throttle** | Left stick – Up/Down | Engine power | More throttle = faster / more climb |
| **Aileron** | Right stick – Left/Right | Roll (bank) | Left = bank left; Right = bank right |
| **Elevator** | Right stick – Up/Down | Pitch (nose attitude) | Up = nose up (climb); Down = nose down (descend) |
| **Rudder** | Left stick – Left/Right | Yaw (nose direction) | Left = nose yaws left; Right = nose yaws right |

**Coordinated Turns – The Most Important Skill**

| **Why Coordination Matters**  A banked turn requires BOTH aileron (to bank) and elevator (to maintain altitude).  When an aircraft banks, the lift vector tilts sideways — some lift is now being used to turn rather than support the aircraft's weight.  To compensate, the pilot must increase back pressure on the elevator to 'load' the turn and maintain altitude.  A turn with aileron only, and no elevator, results in the nose dropping — a common beginner mistake.  Rudder is added in small amounts to prevent 'adverse yaw' — a tendency for the nose to yaw opposite to the direction of roll. |
| --- |

**Why Simulator Training?**

* Real aircraft crashes are expensive, dangerous, and demoralising for new students
* A simulator allows unlimited attempts at any manoeuvre with zero consequence
* The muscle memory and control intuition developed in a simulator transfers directly to real aircraft
* All professional pilots undergo simulator training before flying real aircraft — military, commercial, and private
* The Ghana Civil Aviation Authority (GCAA) recognises simulator time toward pilot training hours

---

## 1.5 Pre Flight Safety Checklist

**Why Checklists Are Not Optional**

Human memory is fallible — especially under time pressure, fatigue, or distraction. Aviation checklists were introduced after a series of accidents in the 1930s caused by experienced pilots forgetting critical steps during routine procedures. The checklist removes reliance on memory and replaces it with a verifiable, accountable system.

| **The Cost of Skipping a Check**  1972 Eastern Air Lines Flight 401: A landing gear indicator light failure distracted the entire flight deck crew. While they investigated the light, nobody was flying the aircraft. It descended slowly into the Florida Everglades. 101 people died.  Root cause: Loss of situational awareness; no one was following their assigned checklist procedure.  Lesson: Checklists exist precisely because intelligent, experienced professionals still make critical errors under pressure. |
| --- |

**The 10-Point Inspection – Reference Table**

Memorise this sequence. Perform it in this exact order, every time.

| **#** | **Check Item** | **What to Look For** | **Status** |
| --- | --- | --- | --- |
| **1** | **Fuselage** | Cracks, dents, loose parts, structural damage, delamination of foam |  |
| **2** | **Wing** | Deformation, warps, loose attachments, leading edge damage |  |
| **3** | **Tail Assembly** | Loose horizontal or vertical stabilizer, cracks at root joints |  |
| **4** | **Control Surfaces** | Freedom of movement, correct trim alignment, no binding or slop |  |
| **5** | **Propeller** | Chips, cracks, secure mounting, balanced spin when turned by hand |  |
| **6** | **Motor / ESC** | Secure mounting, no loose wires, no burn marks, connections tight |  |
| **7** | **Battery** | Secure in tray, correct charge level, no swelling or damage to casing |  |
| **8** | **Receiver** | Antenna fully extended and secured, all servo leads connected firmly |  |
| **9** | **Landing Gear** | Secure mounting, no cracks, wheels spin freely |  |
| **10** | **Overall Check** | No loose parts, no debris on control surfaces, area is clear |  |

**Real Aviation Applications**

* Commercial pilots: Perform a walk-around before every departure, regardless of how many flights they have done
* Maintenance engineers: Use checklists for every repair and inspection; sign each step as it is completed
* Air Traffic Controllers: Use checklists for every handoff, frequency change, and emergency procedure
* GCAA requirement: All aircraft operating in Ghana must have a completed maintenance release (a form of checklist sign-off) before every flight

---

## 1.6 Aircraft Classification

**The Seven Categories of Aircraft**

Aviation classifies all flying vehicles into seven major categories based primarily on how they generate lift and whether they operate within or beyond Earth's atmosphere.

| **Category** | **Type** | **Examples** |
| --- | --- | --- |
| **Fixed-Wing** | Conventional aircraft | Cessna 172, Boeing 737, F-16 Fighting Falcon, Northrop B-2 Spirit |
| **Rotary-Wing** | Helicopters & autogyros | Bell 206, Sikorsky Black Hawk, Robinson R22 |
| **Lighter-Than-Air** | Buoyancy-based lift | Hot air balloon, airship (Zeppelin), blimp |
| **Powered Lift** | Hybrid VTOL | V-22 Osprey, F-35B STOVL, Harrier Jump Jet |
| **Gliders & Sailplanes** | Unpowered fixed-wing | Schweizer 2-33, DG-1000, hang glider |
| **Unmanned Aerial Vehicles** | No onboard pilot | DJI Phantom, MQ-9 Reaper, Boeing ScanEagle |
| **Spacecraft** | Beyond atmosphere | SpaceX Falcon 9, Soyuz capsule, Space Shuttle |

**How Lift is Generated – A Quick Comparison**

* Fixed-wing: Aerofoil wing shape + forward speed (Bernoulli + angle of attack)
* Rotary-wing: Spinning rotor blades — the rotor is a rotating wing
* Lighter-than-air: Buoyancy — the craft is filled with a gas lighter than air (helium or hot air)
* Powered lift: A hybrid — uses jet thrust or rotor wash to take off vertically, then transitions to wing lift
* Gliders: Gravity + aerofoil — trades altitude for forward motion; no engine
* UAV: Any of the above, but controlled remotely or autonomously
* Spacecraft: Does not rely on aerodynamic lift — uses rocket thrust to escape Earth's gravity

**Aviation in Ghana & West Africa**

Including local aviation context makes classification immediately relevant. Here are key examples to include on your poster:

| **Organisation / Aircraft** | **Relevance to Ghana** |
| --- | --- |
| **Africa World Airlines** | Ghanaian carrier; operates ATR 72-600 turboprops and Embraer 170 regional jets |
| **Passion Air** | Ghanaian low-cost carrier; operates Airbus A320 and A319 narrow-body jets |
| **Ghana Air Force** | Operates fixed-wing trainers and transport aircraft; headquartered at Burma Camp, Accra |
| **Kotoka International Airport** | Ghana's primary international hub; serves wide-body jets including Boeing 777 and Airbus A330 |
| **GCAA Flight Academy** | Ghana Civil Aviation Authority training centre; trains Ghanaian pilots and engineers |

| **Did You Know?**  Kotoka International Airport handles over 2 million passengers per year and is served by over 20 international airlines.  Africa World Airlines, founded in 2012, was the first Ghanaian airline to operate scheduled regional jet services.  The Ghana Air Force operates from Accra, Kumasi, and Tamale, and participates in UN peacekeeping air operations across Africa. |
| --- |

---

## 1.7 Four Forces Demonstration

**The Four Forces of Flight**

| **Force** | **Direction** | **Source** | **Real Aircraft Example** |
| --- | --- | --- | --- |
| **Lift** | Upward | Curved wing (Bernoulli + angle of attack) | Wing generates lift in forward flight |
| **Weight** | Downward | Gravity acting on aircraft mass | Heavier aircraft needs more lift |
| **Thrust** | Forward | Engine, propeller, or hand-launch | Fan simulates airstream; hand = thrust |
| **Drag** | Backward | Air resistance on all surfaces | Streamlined shapes reduce drag |

**Airfoil Comparison**

| **Airfoil** | **Streamer Pattern** | **Lift at 0°** | **Use Case** |
| --- | --- | --- | --- |
| **Symmetric** | Even flow top & bottom | Minimal | Aerobatic aircraft; helicopter rotor |
| **Cambered** | Faster top, slower bottom | Good | Commercial aircraft; gliders; trainers |
| **Flat Plate** | Turbulent behind trailing edge | Poor | Educational baseline; kites |

|  |
| --- |
| **Bernoulli's Principle**  When air speeds up, its pressure decreases.  A cambered wing forces air over a longer curved path on top — air speeds up — pressure drops.  Higher pressure below the wing pushes upward: this is LIFT.  At high angles of attack, airflow separates from the surface — this is a STALL. |

**Why Three Airfoil Types?**

* Symmetric: Used on aerobatic aircraft and helicopter rotors — no lift bias; flies equally inverted
* Cambered: Used on most trainers, gliders, and commercial aircraft — efficient lift at cruise speeds
* Flat plate: Educational baseline showing the consequence of no airfoil shaping — high drag, poor lift

---

## 1.8 Centre Of Gravity

**Centre of Gravity vs. Aerodynamic Centre**

The Centre of Gravity (CG) is where all of the aircraft's weight acts downward. The Aerodynamic Centre (AC) is where all the lift force effectively acts. Their relative positions determine whether the aircraft is stable, neutral, or unstable.

|  |
| --- |
| **The Golden Rule of Aircraft Stability**  For static stability: CG must be AHEAD of (forward of) the Aerodynamic Centre.  If the nose drops, a forward CG creates a restoring moment — the aircraft pitches back to level.  If the CG is behind the AC, a nose drop causes the aircraft to pitch further down — unrecoverable dive. |

**Stability Classification**

| **Stability Type** | **Behaviour After Disturbance** | **Aircraft Example** | **CG Position** |
| --- | --- | --- | --- |
| **Stable** | Returns to original level position | Trainer aircraft; commercial jets | Forward of aerodynamic centre |
| **Neutral** | Stays at new disturbed position | Some aerobatic aircraft | At aerodynamic centre |
| **Unstable** | Diverges further from original | Fighter jets (fly-by-wire corrects) | Behind aerodynamic centre |

**Real Aviation – Weight & Balance**

* Every commercial flight has a Load and Trim Sheet prepared by engineers before departure
* The sheet calculates CG from passenger seat assignments, cargo loading, and fuel quantity
* If calculated CG falls outside certified limits, cargo must be moved before departure
* Ghana's Africa World Airlines, like all ICAO carriers, must file a Weight & Balance manifest for every flight

---

## 1.9 Paper Helicopter

**Rotary Aerodynamics**

* Autorotation: as the helicopter falls, air flows upward through the rotor disk. The rotor blades are angled so this upward flow creates a rotation — converting gravitational potential energy into rotor spin
* Drag: the spinning rotor disk creates drag that slows the descent — the same principle as a parachute, but with rotation
* Rotor area: larger rotors intercept more air and generate more drag, slowing descent
* Symmetry: symmetric rotors create equal drag on both sides, producing smooth stable rotation; asymmetric rotors create unequal drag, causing wobble

| **Real Aviation Connection**  When a real helicopter's engine fails, the pilot immediately lowers the collective pitch lever.  This allows the rotor blades to autorotate — air flowing upward through the descending rotor keeps the blades spinning at safe speed.  Just before touchdown, the pilot flares the nose and applies collective pitch, using stored rotor energy to cushion the landing.  Our paper helicopter demonstrates exactly the same energy conversion: gravitational potential → rotor kinetic energy → drag-limited descent. |
| --- |

---

## 2.1 Mini Avionics Bay

**Avionics Concepts**

* Altimeter: Measures altitude above ground level (AGL). Real aircraft use barometric pressure sensors. We simulate with ultrasonic distance to a surface below
* Attitude Indicator (AI): Shows pitch and roll relative to the horizon. The MPU6050 gyroscope measures angular acceleration in all three axes
* Master Caution System: In real cockpits, a Master Caution light alerts the pilot when a system exceeds a limit. Our LED and buzzer system mirrors this

|  |
| --- |
| **I2C Protocol – How Two Devices Share Two Wires**  I2C (Inter-Integrated Circuit) allows multiple devices on just two wires: SDA (data) and SCL (clock).  Each device has a unique address (e.g. OLED = 0x3C, MPU6050 = 0x68).  The ESP32 (master) broadcasts an address; only the matching device (slave) responds.  This is why OLED and MPU6050 can share GPIO 21 and GPIO 22 without conflict. |

**Wiring Reference Table**

| **Component** | **Pin/Signal** | **ESP32 GPIO** | **Notes** |
| --- | --- | --- | --- |
| **Ultrasonic Sensor** | VCC | 5V | Use 5V rail |
| **Ultrasonic Sensor** | GND | GND |  |
| **Ultrasonic Sensor** | TRIG | GPIO 2 | Digital output |
| **Ultrasonic Sensor** | ECHO | GPIO 4 | Digital input |
| **MPU6050 Gyroscope** | VCC | 3.3V | Must use 3.3V only – not 5V |
| **MPU6050 Gyroscope** | GND | GND |  |
| **MPU6050 Gyroscope** | SDA | GPIO 21 | I2C Data line |
| **MPU6050 Gyroscope** | SCL | GPIO 22 | I2C Clock line |
| **OLED Display** | VCC | 3.3V | Shares I2C bus with MPU6050 |
| **OLED Display** | GND | GND |  |
| **OLED Display** | SDA | GPIO 21 | I2C address: 0x3C or 0x3D |
| **OLED Display** | SCL | GPIO 22 |  |
| **Red LED** | Anode (long leg) | GPIO 5 | 330Ω resistor in series |
| **Green LED** | Anode (long leg) | GPIO 18 | 330Ω resistor in series |
| **Yellow LED** | Anode (long leg) | GPIO 19 | 330Ω resistor in series |
| **Active Buzzer** | Positive leg | GPIO 23 | Active type only – no resistor |

**Alert Logic Table**

| **Parameter** | **Normal Range** | **Alert Threshold** | **Indicator** | **Display Message** |
| --- | --- | --- | --- | --- |
| **Altitude (simulated)** | 50–200 cm | < 30 cm | Red LED + Buzzer | LOW ALT |
| **Pitch Angle** | –15° to +15° | ±25° | Yellow LED + Buzzer | ATT WARN |
| **Roll Angle** | –15° to +15° | ±25° | Yellow LED + Buzzer | ATT WARN |
| **All Normal** | All in range | — | Green LED steady | ALL OK |

---

## 2.10 Jet Engine Principles

**The Brayton Thermodynamic Cycle**

| **Stage** | **What Happens** | **Temperature Change** | **Pressure Change** | **Component** |
| --- | --- | --- | --- | --- |
| **1 – Intake** | Air drawn into engine | Slight increase | Slight increase | Inlet duct |
| **2 – Compression** | Air compressed mechanically | Large increase (+300°C) | Large increase (×30) | Compressor |
| **3 – Combustion** | Fuel added; air-fuel mix ignited | Very large increase (+1000°C) | Constant (approx.) | Combustion chamber |
| **4 – Expansion** | Hot gas expands through turbine | Decreases (work extracted) | Drops | Turbine |
| **5 – Exhaust** | Gas expelled at high speed | Further decrease | Returns to ambient | Nozzle |

|  |
| --- |
| **Newton's Third Law – Rocket & Jet Engine**  Jet engine: air is accelerated rearward at high speed (action). The engine — and aircraft — is pushed forward (reaction).  Water rocket: water is expelled downward at high speed (action). The rocket is pushed upward (reaction).  Both systems demonstrate the same physics: F = ṁ × ΔV (thrust = mass flow rate × velocity change).  The key difference: a jet engine operates continuously; a water rocket exhausts all propellant in the first 0.5 seconds. |

**Rocket Variable Data Table**

| **Variable** | **Test 1** | **Test 2** | **Test 3** | **Notes** |
| --- | --- | --- | --- | --- |
| **Water fill level (%)** |  |  |  | 25%, 50%, or 75% |
| **Launch angle (°)** |  |  |  | 45°, 60°, or 75° |
| **Max height (m)** |  |  |  | Estimate from visual |
| **Horizontal distance (m)** |  |  |  | Measure with tape |
| **Fin area (relative)** |  |  |  | Small/medium/large |

---

## 2.12 Water Bottle

**Rocket Physics**

* Newton's Third Law: water is expelled downward at high velocity (action); rocket is pushed upward (reaction)
* Thrust: F = ṁ × v\_exit. Thrust depends on mass flow rate (how much water per second) and exit velocity (how fast)
* Optimal fill: too little water → low mass flow rate → low thrust. Too much water → little compressed air volume → short thrust duration and low pressure differential
* Fins: act as a pendulum moment — drag on fins (which are behind the CG) stabilises the rocket and prevents spin
* Pressure: higher pressure → higher exit velocity → higher thrust → more height. But diminishing returns above 80 PSI as the rubber seal limits flow

|  |
| --- |
| **Rocket vs Jet Engine – Key Comparison**  SIMILARITY: Both generate thrust by Newton's Third Law — expelling mass rearward at high velocity.  DIFFERENCE 1: A jet engine uses atmospheric oxygen for combustion. A rocket carries its own oxidiser, so it can operate in space where there is no atmosphere.  DIFFERENCE 2: A jet engine operates continuously at steady state. A water rocket exhausts all propellant in 0.3–0.5 seconds, then becomes an unpowered projectile.  REAL WORLD: The Ariane 5 rocket that launched Ghana's first satellite (GhanaSat-1 in 2017) used the same action-reaction principle as this water rocket. |

---

## 2.13 Gyroscope Accelerometer

**Instrument to Sensor Mapping**

| **Real Aircraft Instrument** | **Axis Measured** | **Sensor in This Project** | **Display Output** |
| --- | --- | --- | --- |
| **Attitude Indicator (AI)** | Pitch + Roll | MPU6050 Accel + Gyro | Bar graph: pitch –90° to +90°; roll –180° to +180° |
| **Turn Coordinator** | Yaw rate + Roll | MPU6050 Gyro Z + Y | Rate needle: –3°/s (left) to +3°/s (right) |
| **Inclinometer (Ball)** | Lateral acceleration | MPU6050 Accel X | Ball position: left/right of centre |
| **Rate-of-Turn** | Yaw rate | MPU6050 Gyro Z | Numeric display: °/s |
| **Heading Indicator** | Yaw (relative) | MPU6050 Gyro Z integrated | Compass rose: 0–360° |

|  |
| --- |
| **Why Two Sensors Are Better Than One**  A gyroscope measures angular RATE (°/s) — integrating rate over time gives angle, but errors accumulate (drift).  An accelerometer measures acceleration in all three axes — when stationary, it measures gravity direction accurately, but it is noisy during motion.  The complementary filter combines both: gyro for fast, smooth changes; accelerometer for long-term correction.  This is identical to the sensor fusion algorithm inside the MPU6050 used in the Project 10 quadcopter's flight controller.  Advanced systems (Kalman Filter) do the same thing mathematically — the complementary filter is the simplified, intuitive version. |

---

## 2.2 Build A Tethered

**Motor Configuration**

| **Motor #** | **Position** | **Spin Direction** | **Propeller Type** |
| --- | --- | --- | --- |
| **M1** | Front Left | Clockwise (CW) | CW threaded propeller |
| **M2** | Front Right | Counter-Clockwise (CCW) | CCW threaded propeller |
| **M3** | Rear Right | Clockwise (CW) | CW threaded propeller |
| **M4** | Rear Left | Counter-Clockwise (CCW) | CCW threaded propeller |

**Four Control Inputs**

| **Input** | **Stick** | **Motors Affected** | **Effect** |
| --- | --- | --- | --- |
| **Throttle** | Left – Up/Down | All 4 equally | Climb or descend |
| **Roll** | Right – Left/Right | Left pair up / Right pair down (or vice versa) | Bank left or right |
| **Pitch** | Right – Up/Down | Front pair up / Rear pair down (or vice versa) | Nose up or nose down |
| **Yaw** | Left – Left/Right | CW pair up / CCW pair down (or vice versa) | Rotate clockwise or counter-clockwise |

|  |
| --- |
| **Why Alternating CW/CCW Motors?**  Each spinning motor creates a torque reaction that would rotate the drone in the opposite direction.  Two CW + two CCW motors cancel the torques — the drone stays pointed forward.  To YAW: the FC increases CW pair speed and reduces CCW pair (or vice versa) — unbalanced torque rotates the drone. |

---

## 2.3 Scratch Built Foam Board

**Control Surfaces & Inputs**

| **Surface** | **Servo Location** | **Stick Input** | **Aircraft Response** |
| --- | --- | --- | --- |
| **Ailerons** | Outer wing trailing edge | Right stick Left/Right | Roll left or right |
| **Elevator** | Horizontal stabilizer trailing edge | Right stick Up/Down | Pitch nose up or down |
| **Rudder (optional)** | Vertical stabilizer trailing edge | Left stick Left/Right | Yaw nose left or right |
| **Throttle** | ESC connected to motor | Left stick Up/Down | Increase or decrease speed |

|  |
| --- |
| **Score-and-Fold Airfoil**  Foam board has a paper skin on both sides and a foam core.  Scoring — cutting through one paper layer without cutting the foam — allows the board to curve.  When scored face is on the inside of the fold, the outer paper skin creates a smooth curved surface.  This produces a simple but effective cambered airfoil that generates real lift. |

---

## 2.4 Rc Plane

**Figure-8 Technique Guide**

| **Manoeuvre** | **Inputs Required** | **Common Error** | **Correction** |
| --- | --- | --- | --- |
| **Entry to turn** | Aileron to bank; elevator to maintain altitude | No elevator — nose drops | Add back pressure as you bank |
| **Holding the turn** | Sustained aileron; continuous elevator | Over-banking; losing height | Reduce bank; add more elevator |
| **Rollout** | Opposite aileron; reduce elevator | Overshooting the exit heading | Start rollout 10° before target heading |
| **Crossover (centre)** | Level wings; check altitude | Too high or too low at crossover | Correct throttle on downwind leg before crossover |
| **Wind correction** | Crab angle into wind | Drift off intended track | Point nose slightly into wind; hold the heading |

|  |
| --- |
| **The Coordinated Turn – Key Concept**  A banked turn requires THREE simultaneous inputs: aileron (to bank), elevator (to maintain altitude), and slight rudder (to prevent adverse yaw).  In a 30° banked turn, 15% of the wing's lift is being used to turn rather than support weight — add elevator to compensate.  The steeper the bank, the more elevator is needed. A 60° bank requires twice the lift of level flight.  Failing to add elevator is the most common beginner error — the nose drops and altitude is lost. |

**Wind Correction**

* Wind pushes the aircraft sideways relative to the intended ground track
* Correction: point the nose slightly into wind (crab angle) so sideways drift cancels the crosswind
* Into-wind turns are tighter (less ground distance); downwind turns are wider
* Plan circuit geometry with the wind in mind: fly tighter patterns on into-wind legs

---

## 2.5 Cockpit Instrument Panel

**Instrument Panel Functions**

| **Instrument** | **Sensor** | **Display Value** | **Real Aircraft Equivalent** |
| --- | --- | --- | --- |
| **Altimeter** | BMP280 Barometric Pressure | Altitude in metres (m) | Barometric altimeter (QNH/QFE) |
| **Attitude Indicator** | MPU6050 Gyro/Accel | Pitch (°) and Roll (°) | Artificial Horizon (ADI) |
| **Heading Indicator** | QMC5883L Compass | Magnetic heading (0–360°) | Directional Gyro / HSI |
| **Position** | NEO-6M GPS | Latitude, Longitude, Speed | GPS/GNSS navigation display |
| **Variometer** | BMP280 (rate of change) | Climb/Descent rate (m/s) | Vertical Speed Indicator (VSI) |

**Communication Protocols in Use**

* I2C (GPIO 21/22): Used for BMP280, MPU6050, and QMC5883L — suitable for slow sensor data; up to 127 devices on two wires
* SPI (GPIO 18/23/5/4): Used for the TFT display — fast protocol needed for screen pixel updates at 60+ Hz
* UART (GPIO 2/3): Used for GPS — streams NMEA sentence strings at 9600 baud; parsed by TinyGPS++ library

|  |
| --- |
| **The T-Scan Instrument Layout**  Real aircraft cockpits follow the Basic T layout: Attitude Indicator centre top, Airspeed left, Altimeter right, Heading Indicator below centre.  Pilots are trained to scan in a T pattern — primary instruments are always in the same position so they can be found instantly under stress.  Our panel uses the same principle: attitude indicator is the largest and most central instrument; altitude and heading flank it.  Consistent layout reduces pilot workload and is mandated by ICAO standards for certified aircraft. |

**Panel Layout Design**

| **Panel Zone** | **Instrument(s)** | **Position on Faceplate** | **Priority** |
| --- | --- | --- | --- |
| **Top Centre** | Attitude Indicator | Largest element; primary scan | 1 – Critical |
| **Top Left** | Altimeter | Upper left quadrant | 2 – Primary |
| **Top Right** | Heading Indicator | Upper right quadrant | 2 – Primary |
| **Bottom Left** | Variometer | Lower left quadrant | 3 – Secondary |
| **Bottom Centre** | GPS Position | Lower centre strip | 3 – Secondary |
| **Bottom Right** | System Status (GPS fix, battery) | Lower right corner | 4 – Advisory |

|  |
| --- |
| **Complementary Filter – Fixing Gyroscope Drift**  A gyroscope measures angular rate (how fast you are turning) — integrating this over time gives angle.  Problem: small errors accumulate over time (drift) — after 60 seconds, the attitude reading is wrong.  Solution: the accelerometer measures gravity direction and always knows 'down' — accurate but noisy.  Complementary filter: angle = 0.98 × (gyro\_angle) + 0.02 × (accel\_angle)  This blends 98% gyroscope (smooth, short-term accurate) with 2% accelerometer (long-term stable). |

---

## 2.7 Led Navigation

**ICAO Navigation Light Standards**

| **Light** | **Colour** | **Position** | **Arc** | **Meaning** |
| --- | --- | --- | --- | --- |
| **Port navigation** | Red | Left wingtip | 110° forward arc | Aircraft's left side |
| **Starboard navigation** | Green | Right wingtip | 110° forward arc | Aircraft's right side |
| **Tail navigation** | White | Tail | 140° rear arc | Aircraft viewed from behind |
| **Anti-collision strobe** | White or Red | Fuselage top/bottom | 360° | Flashing; warns other aircraft |
| **Landing light** | White | Nose/wing leading edge | Forward | Illuminates runway on approach |

**Wiring Reference Table**

| **LED** | **GPIO** | **Resistor** | **Behaviour** | **ICAO Colour** |
| --- | --- | --- | --- | --- |
| **Port LED** | GPIO 5 | 470Ω | Steady on during flight | Red |
| **Starboard LED** | GPIO 18 | 470Ω | Steady on during flight | Green |
| **Tail LED** | GPIO 19 | 470Ω | Steady on during flight | White |
| **Anti-collision Strobe** | GPIO 23 | 470Ω | Flashing: 40 flashes/min | White |
| **Landing Light** | GPIO 21 | 470Ω | On demand via switch (CH6) | White |

|  |
| --- |
| **Why These Colours? – The Rules of the Air**  ICAO Annex 2 (Rules of the Air) mandates navigation light colours internationally.  Red on the left (port) and green on the right (starboard) are derived from maritime navigation rules — aircraft inherited the same convention.  A pilot seeing BOTH red and green simultaneously knows an aircraft is flying directly toward them — the most critical awareness possible.  A pilot seeing only WHITE is following another aircraft from behind — overtaking rules apply.  These colours are used at Kotoka International Airport, on every domestic Passion Air and Africa World Airlines flight, and on all aircraft worldwide. |

---

## 2.8 Altitude Climb Rate

**How a Barometric Altimeter Works**

* Atmospheric pressure decreases with altitude at approximately 1 hPa per 8 metres at low altitude
* The BMP280 measures absolute pressure (hPa) and converts to altitude using the International Standard Atmosphere (ISA) model
* The ISA assumes sea-level pressure = 1013.25 hPa and temperature = 15°C — in Ghana, actual conditions often differ

|  |
| --- |
| **Density Altitude Formula**  Density altitude accounts for the actual effect of temperature and pressure on air density — this is what matters for aircraft performance.  Density Altitude (ft) = Pressure Altitude (ft) + 120 × (OAT\_°C – ISA\_Temp\_°C)  ISA Temperature at any altitude = 15°C – (2°C × altitude\_in\_thousands\_of\_feet)  Example: Accra elevation = 213 ft; OAT = 30°C; ISA Temp at 213 ft ≈ 15°C  Density Altitude = 213 + 120 × (30 – 15) = 213 + 1800 = 2013 ft  Practical implication: your aircraft performs as if it is at 2013 ft even though you are only 213 ft above sea level. |

**Instrument Comparison**

| **Real Instrument** | **Variable Measured** | **Sensor in This Project** | **Display** |
| --- | --- | --- | --- |
| **Altimeter (Barometric)** | Altitude above QNH datum | BMP280 pressure sensor | OLED + SD card log |
| **Vertical Speed Indicator (VSI)** | Rate of climb/descent (m/s) | BMP280 (rate of altitude change) | OLED + SD card log |
| **Outside Air Temperature** | Temperature in °C | BMP280 temperature sensor | Serial monitor |
| **Density Altitude Calculator** | Effect of temp/pressure on performance | Computed from BMP280 data | Calculated post-flight |

---

## 2.9 Aviation Weather

**Weather Parameters & Aviation Effects**

| **Parameter** | **Sensor** | **Unit** | **How It Affects Aircraft Performance** |
| --- | --- | --- | --- |
| **Temperature** | DHT22 / BMP280 | °C | Higher temp = lower air density = reduced lift and engine power |
| **Relative Humidity** | DHT22 | % | High humidity reduces effective air density (water vapour is lighter than dry air) |
| **Barometric Pressure** | BMP280 | hPa | Lower pressure = lower air density = higher density altitude |
| **Wind Speed** | Anemometer cup | km/h | Headwind helps takeoff; tailwind requires longer runway |
| **Wind Direction** | Wind vane / compass | ° | Crosswind component determines usable runway |

|  |
| --- |
| **METAR – The Global Aviation Weather Code**  METAR (Meteorological Aerodrome Report) is the international standard weather observation format.  Issued every 30 minutes at major airports; every hour at smaller stations.  Used by pilots for pre-flight weather briefing; by ATC for runway selection; by dispatchers for fuel calculation.  Every operational airport in Ghana, including Kotoka (DGAA), Kumasi (DGSI), and Tamale (DGLE), issues METAR reports.  Understanding a METAR is a core competency for all aviation personnel — pilots, controllers, engineers, and dispatchers. |

---

## 3.1 Fpv Quadcopter

**FPV System Components**

| **Component** | **Role** | **Key Spec** | **Notes** |
| --- | --- | --- | --- |
| **FPV Camera** | Captures live video | 600–1000 TVL or HD | Wide-angle lens; 120–160° FOV preferred |
| **Video Transmitter (VTX)** | Broadcasts video wirelessly | 5.8 GHz; 25–200 mW | Lower power = less heat; check local regulations |
| **Antenna (VTX)** | Transmits signal to goggles | Circular polarised (cloverleaf) | Mount vertically; clear of frame arms |
| **FPV Goggles / Monitor** | Receives and displays video | Matched to 5.8 GHz | Diversity receiver preferred for range |
| **Spotter** | Eyes-on safety observer | Human | Mandatory during all FPV flights – not a component but a role |

**Frequency & Channel Reference**

| **Band** | **Channels** | **Frequencies (MHz)** | **Notes** |
| --- | --- | --- | --- |
| **Raceband (R)** | R1–R8 | 5658–5917 | Most popular for racing and freestyle |
| **Band A** | A1–A8 | 5865–5945 | Fatshark default; good for beginners |
| **Band B** | B1–B8 | 5733–5840 | Often used for second pilot in same area |
| **Band E** | E1–E8 | 5705–5885 | Avoid E4 and E5 – close to Wi-Fi channels |

|  |
| --- |
| **Latency – Why It Matters for FPV**  Latency is the delay between what the camera sees and what the pilot sees in the goggles.  Analogue 5.8 GHz systems have < 40 ms latency — fast enough to feel real-time.  Digital HD systems (DJI, HDZero, Walksnail) have 20–50 ms latency — comparable to analogue.  High latency (> 100 ms) makes the drone feel sluggish and hard to control — the pilot reacts to what already happened.  This is why commercial FPV systems are engineered to minimise latency, not maximise image quality. |

**Spatial Awareness in FPV**

* Without peripheral vision, depth perception is reduced — distances feel different through goggles
* Building a mental 3D map of the environment is the core skill in FPV flying
* Looking toward a gate before flying toward it — called 'spotting the gate' — is used by all skilled FPV pilots
* When disoriented: reduce throttle slowly to land; do not make sudden inputs

---

## 3.10 Dead Reckoning

**Dead Reckoning Navigation Concepts**

* True Course: the direction from departure to destination measured on a chart from True North
* Magnetic Variation: the difference between True North and Magnetic North at any given location; in Ghana, approximately 3° West (subtract 3° from true heading to get magnetic heading)
* Wind Correction Angle (WCA): the angle the aircraft must point into the wind to maintain the desired track over the ground
* Groundspeed: the aircraft's actual speed over the ground = True Airspeed ± wind component along the track

|  |
| --- |
| **Why Pilots Still Learn Dead Reckoning**  GPS satellites can be jammed, spoofed, or fail entirely — this has happened over conflict zones and been tested by adversaries.  ICAO requires all instrument-rated pilots to demonstrate dead reckoning proficiency.  The Ghana Civil Aviation Authority (GCAA) includes navigation theory in all pilot licence examinations.  A pilot who cannot navigate without GPS is dependent on a single point of failure — unacceptable in aviation where redundancy is a core safety principle. |

---

## 3.11 Ads B Live Aircraft

**Surveillance Technology Comparison**

| **System** | **Type** | **Range** | **How It Works** | **Aviation Use** |
| --- | --- | --- | --- | --- |
| **Primary Radar** | Ground-based | 200+ nm | Transmits RF pulses; detects reflected signal from aircraft | ATC – detects all aircraft including non-cooperative |
| **Secondary Radar (SSR)** | Ground-based | 250 nm | Queries aircraft transponder; aircraft replies with code + altitude | ATC – adds identity and altitude to radar return |
| **ADS-B Out** | Airborne | 150+ nm (air-to-air) | Aircraft broadcasts GPS position, ID, altitude, speed via 1090 MHz | ATC + other aircraft; basis of modern surveillance |
| **TCAS (ACAS)** | Airborne | ±6 nm | Queries nearby transponders; issues climb/descend advisories | Collision avoidance on all commercial aircraft |
| **ADS-B In** | Airborne | 150 nm | Receives ADS-B Out from other aircraft; displays on cockpit screen | Situational awareness; traffic display |

|  |
| --- |
| **Why ADS-B is Revolutionising African Aviation**  Traditional radar requires expensive rotating antenna arrays, high-power transmitters, and specialist maintenance.  ADS-B ground stations cost 100× less to install and can provide identical coverage in flat terrain.  ICAO mandated ADS-B Out on all aircraft in most airspace classes by 2020.  Ghana's GCAA has been a leader in African ADS-B implementation — coverage now extends across much of West Africa.  The result: more aircraft can be tracked more accurately, with less infrastructure, improving safety across the region. |

---

## 3.12 Aircraft Maintenance

**Maintenance Types Reference**

| **Type** | **Interval** | **Description** | **Example Tasks** |
| --- | --- | --- | --- |
| **Pre-flight** | Before every flight | Visual and functional inspection | 10-point checklist from Project 5; control surface check |
| **Post-flight** | After every flight | Damage check; log unusual events | Inspect for cracks, loose joints, prop damage; update log |
| **Periodic (50 hr)** | Every 50 flying hours | Deeper inspection of key systems | Re-tension all screws; check ESC solder joints; clean motors |
| **Annual** | Every 12 months | Full structural and systems inspection | Measure all deflections; check battery health; replace worn parts |
| **On-condition** | When triggered by event | Inspect after hard landing, crash, or unusual behaviour | Post-crash structural check; motor bearing test; frame inspection |

**Task Reference Table**

| **Task Ref** | **Task Description** | **Category** | **Special Tools** | **Est. Time** |
| --- | --- | --- | --- | --- |
| **T-01** | Inspect all frame arms for cracks and deformation | Pre-flight | Naked eye | 2 min |
| **T-02** | Check all motor screws for tightness | Post-flight / 50 hr | M3 hex driver | 3 min |
| **T-03** | Clean motor windings with compressed air | 50 hr | Air duster | 5 min |
| **T-04** | Check ESC solder joints under magnification | 50 hr | Magnifier, multimeter | 10 min |
| **T-05** | Load-test LiPo battery under 10A draw | Annual | Watt meter | 5 min |
| **T-06** | Calibrate compass after any crash | On-condition | Flight controller software | 5 min |
| **T-07** | Replace propellers | On-condition | Prop wrench | 3 min |
| **T-08** | Measure and record control surface deflection angles | Annual | Protractor | 10 min |

|  |
| --- |
| **Why Maintenance Logging Matters**  The 1988 Aloha Airlines Flight 243 accident — where a large section of fuselage separated in flight — was partly attributed to inadequate maintenance record-keeping and inspection procedures.  The accident directly led to ICAO strengthening Annex 6 maintenance documentation requirements.  Every aircraft with a valid Certificate of Airworthiness has a complete, unbroken maintenance log dating from its first flight.  Ghana's AMEs (Aircraft Maintenance Engineers) are required to sign maintenance entries under GCAA Part 66 — their licence is at risk if entries are inaccurate. |

---

## 3.13 Flight Data Recorder

**FDR Parameter Comparison**

| **Parameter** | **Real Aircraft FDR** | **This Project's FDR** | **Sample Rate** |
| --- | --- | --- | --- |
| **Altitude** | Barometric + GPS | BMP280 barometric | 2 Hz |
| **Pitch & Roll** | Gyro + Accelerometer | MPU6050 (complementary filter) | 10 Hz |
| **G-Force** | 3-axis accelerometer | MPU6050 AccX/Y/Z | 10 Hz |
| **Temperature** | OAT probe | BMP280 temperature | 1 Hz |
| **Timestamp** | UTC from GPS | ESP32 millis() counter | Every record |
| **Storage** | Crash-resistant SSFDR | MicroSD card (FAT32) | Continuous |
| **Playback** | DFDR replay system | CSV in Excel/LibreOffice | Post-flight |

|  |
| --- |
| **Real FDR – How It Works**  A modern Solid State Flight Data Recorder (SSFDR) records 25+ hours of flight data to crash-resistant NAND flash memory.  ICAO Annex 6 mandates FDRs on all commercial aircraft above 5,700 kg maximum takeoff weight.  The recorder must survive: 3,400 g impact; 1100°C fire for 30 minutes; 6,000 m submersion for 30 days.  When investigators retrieve the FDR, they replay the data using Digital Flight Data Replay software to reconstruct the entire flight in 3D animation.  This project records the same parameters — altitude, attitude, G-force, temperature — at a lower sample rate and without crash protection. |

---

## 3.2 Autonomous Gps

**How GPS Navigation Works**

* The GPS module receives signals from 4+ satellites to calculate its position to within 1–3 metres
* The flight controller compares current GPS position to the next waypoint's GPS coordinates
* It calculates the required heading and distance, then applies throttle, pitch, and roll to move toward the waypoint
* This loop runs approximately 400 times per second — far faster than any human pilot

|  |
| --- |
| **Coordinate Systems in UAV Navigation**  GPS uses WGS84 coordinates: Latitude (north/south, -90° to +90°) and Longitude (east/west, -180° to +180°).  Altitude in ArduPilot is measured in metres above the home point (takeoff location), not sea level.  Mission Planner displays coordinates in decimal degrees: Accra is approximately 5.5600° N, -0.2057° E.  GPS accuracy of 1–3 m is sufficient for waypoint navigation but NOT for precision landing — that requires additional sensors. |

**Failsafe Systems**

| **Failsafe Type** | **Trigger Condition** | **Drone Action** | **Setting Location** |
| --- | --- | --- | --- |
| **Return to Launch (RTL)** | RC signal lost > 1 s | Climbs to RTL altitude; flies home; lands | Betaflight Failsafe tab |
| **Low Battery RTL** | Battery voltage < 3.5V/cell | Initiates RTL automatically | ArduPilot Battery Monitor |
| **GeoFence Breach** | Drone exits defined boundary | Returns to home point | ArduPilot GeoFence settings |
| **GPS Loss** | GPS fix lost in auto mode | Switches to manual; pilot takes control | ArduPilot GPS Glitch |
| **RC Override** | Pilot flips mode switch | Immediately exits auto; pilot controls | Mode switch on transmitter |

---

## 3.3 Rc Plane Cargo

**Ballistics – Predicting Where the Payload Lands**

When the payload is released, it immediately has two components of velocity: forward (equal to the aircraft speed) and zero vertical (no initial downward velocity). Gravity then accelerates it downward at 9.8 m/s². The payload follows a parabolic path — identical to a thrown ball.

|  |
| --- |
| **Drop Distance Formula (Simplified)**  Time to fall from altitude h: t = √(2h / g) where g = 9.8 m/s²  Forward travel during fall: d = v × t where v = aircraft speed in m/s  Example: flying at 15 m altitude at 20 m/s → t = √(2×15/9.8) = 1.75 s → d = 20 × 1.75 = 35 m ahead  Therefore: release the payload approximately 35 m before the target when flying at 20 m/s at 15 m altitude.  In practice: this is refined through repeated drops and adjustment. |

**Variables Affecting Drop Accuracy**

| **Variable** | **Effect on Drop Point** | **Pilot Control** |
| --- | --- | --- |
| **Aircraft altitude** | Higher altitude = longer forward travel | Fly lower for shorter drop distance |
| **Aircraft speed** | Faster = payload travels further forward | Reduce speed before drop zone |
| **Release point** | Earlier = payload lands further ahead | Release slightly before flying over target |
| **Payload aerodynamics** | Streamlined = less drag = more forward travel | Use compact, symmetrical payload shape |
| **Wind (headwind)** | Payload drifts less forward | Release slightly later than in calm conditions |
| **Wind (tailwind)** | Payload drifts further forward | Release slightly earlier than in calm conditions |

---

## 3.4 Quadcopter Obstacle

**Course Elements & Skills**

| **Element** | **Description** | **Dimensions** | **Skill Tested** |
| --- | --- | --- | --- |
| **Gate A** | Vertical frame; fly through horizontally | 1.5 m wide × 1 m tall | Lateral precision |
| **Gate B** | Vertical frame; fly through horizontally | 1.2 m wide × 1 m tall | Precision at speed |
| **Gate C** | Elevated gate | 1.2 m wide × 1.2 m tall | Altitude management |
| **Slalom 1–4** | Four pylons; weave between them | 1 m spacing | Direction change rate |
| **Landing Zone** | Marked circle on ground | 1 m diameter | Final precision & control |

**Penalty System**

| **Infraction** | **Time Penalty** | **Notes** |
| --- | --- | --- |
| **Touch a gate frame** | + 5 seconds | Confirmed by spotter on that gate |
| **Miss a gate (fly around it)** | + 10 seconds | Gate must be re-flown; add 10 s for missed attempt |
| **Touch the ground outside landing zone** | + 3 seconds | Per touch |
| **Land outside the landing zone** | + 5 seconds | Pilot must take off and re-land within the zone |
| **Hard landing (tip-over)** | + 5 seconds + repair time | Stop clock while repairs made |
| **Fly outside course boundary** | Run disqualified | Must restart from Gate A |

|  |
| --- |
| **Look-Ahead Technique – The Key to Fast, Clean Flying**  Skilled pilots do not look at what they are flying through — they look at what comes NEXT.  By the time the drone reaches Gate A, the pilot's eyes should already be on Gate B.  This gives the pilot time to set up the approach angle, altitude, and speed for the next element.  Looking at the current gate causes late corrections, overshoots, and missed turns.  This technique is identical to the advanced scan technique taught to commercial pilots: 'never fixate; always scan ahead'. |

---

## 3.5 Flaps Spoilers

**High-Lift Device Effects**

| **Configuration** | **Flap Angle** | **Effect on Lift** | **Effect on Drag** | **Use Case** |
| --- | --- | --- | --- | --- |
| **Clean (no flaps)** | 0° | Baseline | Baseline | Cruise; normal flight |
| **Partial flap** | 15° | +20–30% | Moderate increase | Approach; slowing down |
| **Full flap** | 30° | +40–60% | Large increase | Landing; short field |
| **Spoiler deployed** | – | Reduces lift | Large increase | Rapid descent; speed brake |

|  |
| --- |
| **Why Flaps Are Used on Every Landing**  Without flaps, an aircraft must maintain a minimum speed to avoid stalling — this speed determines the minimum runway length needed.  Flaps increase the wing's camber and effective area, generating more lift at lower speeds.  This allows the aircraft to fly the approach at a slower, safer speed without stalling.  A Boeing 737 approaches at approximately 145 knots clean; with full flaps (40°), it can land at 135 knots — saving runway length.  At Kotoka International Airport, every landing aircraft deploys flaps in stages during the approach. |

---

## 3.7 Aircraft Materials

**Aviation Materials Reference Table**

| **Material** | **Density (g/cm³)** | **Tensile Strength (MPa)** | **Specific Strength (MPa·cm³/g)** | **Primary Aircraft Use** |
| --- | --- | --- | --- | --- |
| **Aluminium 6061** | 2.70 | 276 | 102 | Fuselage skin; wing ribs; frames |
| **Carbon Fibre (CFRP)** | 1.60 | 1500+ | 937+ | Spar caps; fuselage shells; rotor blades |
| **Fibreglass (GFRP)** | 2.00 | 440 | 220 | Fairings; doors; secondary structures |
| **Balsa Wood** | 0.16 | 20 | 125 | Model aircraft; core in sandwich panels |
| **EVA Foam** | 0.03–0.06 | 0.5–2 | 15–30 | Model aircraft; cushioning; packaging |
| **Steel (mild)** | 7.85 | 400 | 51 | Landing gear; engine mounts; fasteners |

|  |
| --- |
| **Why Specific Strength Matters More Than Absolute Strength**  A steel beam is stronger than a carbon fibre beam of the same size — but it is also 5× heavier.  In aircraft design, what matters is strength per kilogram of weight — specific strength.  Carbon fibre's specific strength is over 10× that of aluminium and over 18× that of steel.  This is why the Boeing 787 Dreamliner fuselage is 50% carbon fibre by weight — and burns 20% less fuel than the all-aluminium 767.  The trade-off: carbon fibre is expensive, brittle under impact, and difficult to inspect for internal damage. |

---

## 3.8 Moments Stability

**The Three Axes of Flight**

| **Axis** | **Name** | **Motion** | **Control Surface** | **Positive Direction** |
| --- | --- | --- | --- | --- |
| **Longitudinal** | Roll axis | Rolling left or right | Ailerons | Right wing down |
| **Lateral** | Pitch axis | Nose up or nose down | Elevator | Nose up |
| **Normal** | Yaw axis | Nose left or nose right | Rudder | Nose right |

|  |
| --- |
| **Moment Equilibrium in a Trimmed Aircraft**  A trimmed aircraft flies with no tendency to pitch, roll, or yaw without control input.  This requires all moments about each axis to sum to zero.  Pitching: the tail's downforce × tail moment arm = wing lift offset × CG-to-AC distance.  If CG moves forward: nose-down moment increases; pilot must add back pressure to maintain level flight.  If CG moves aft: nose-up moment increases; aircraft becomes less stable and may pitch up uncontrollably.  This is why the load-and-trim sheet from Project 8 is checked before every commercial flight. |

**Moment Calculation Worksheet**

| **Scenario** | **Force (N)** | **Moment Arm (m)** | **Pitching Moment (N·m)** | **Effect** |
| --- | --- | --- | --- | --- |
| **Lift at AC = 0.3 m from CG** | 100 | 0.3 | 30 | Nose-up pitching moment |
| **Tail downforce = 0.9 m from CG** | 10 | 0.9 | 9 | Nose-down pitching moment |
| **Engine thrust 0.2 m below CG** | 200 | 0.2 | 40 | Pitching moment (direction?) |
| **Your design – enter values** |  |  |  |  |

---

## 4.1 Design Build A Custom

**Design Trade-Offs**

| **Design Factor** | **Trade-Off** | **How to Decide** |
| --- | --- | --- |
| **Frame size (larger)** | More stable; longer flight time; less agile; harder to transport | Match to mission: survey needs stability; racing needs agility |
| **Motor KV (higher)** | Faster; more responsive; shorter flight time; more battery drain | Higher KV for racing; lower KV for long-endurance or heavy-lift |
| **Battery capacity (larger)** | Longer flight time; heavier; reduces agility and payload | Calculate: target flight time × average current draw = mAh needed |
| **Frame material (carbon)** | Lighter; stronger; expensive; hard to fabricate without tools | Use if budget allows; otherwise plywood with carbon reinforcement |
| **Propeller size (larger)** | More efficient; more thrust; slower response; risk of ground strikes | Match to motor KV; larger prop needs lower KV motor |
| **Number of motors (6 vs 4)** | More thrust and redundancy; heavier; more complex; more expensive | Use hexacopter for payload > 500g or when one motor failure must not cause crash |

|  |
| --- |
| **The Engineering Design Process**  Define → clearly state the problem and constraints before generating solutions.  Ideate → generate multiple concepts without judging them; quantity before quality.  Select → use evidence (decision matrix) to choose the best concept; do not rely on gut feeling alone.  Prototype → build the simplest version that can be tested; don't optimise prematurely.  Test → measure against the original requirements; use quantified criteria.  Iterate → make one change at a time; test after each change to identify its effect.  Present → engineers must communicate their decisions as clearly as they make them. |

---

## 4.2 Full Capstone

**The Full Engineering Design Cycle – Applied**

* Define: the mission brief states the problem; the requirements state what success looks like
* Research: understanding existing solutions (Zipline, NADMO UAVs) informs better design decisions
* Ideate: the aircraft selection and modification plan explores options before committing
* Select: every major decision should be justified with evidence — not personal preference
* Prototype: practice flights test the system in the real environment before Mission Day
* Test: the mission execution generates real performance data against real success criteria
* Evaluate: the data analysis section compares actual vs planned performance honestly
* Iterate: the reflection section identifies what would be changed in a second mission cycle
* Present: the portfolio and presentation communicate the engineering process to others

---

## 4.3 Servo Controlled

**Control Surface Reference Table**

| **Surface** | **Input** | **Movement** | **Aircraft Effect** |
| --- | --- | --- | --- |
| **Aileron** | Left stick right | Left aileron UP; Right aileron DOWN | Roll right |
| **Aileron** | Left stick left | Left aileron DOWN; Right aileron UP | Roll left |
| **Elevator** | Right stick back | Trailing edge UP | Pitch nose up |
| **Elevator** | Right stick forward | Trailing edge DOWN | Pitch nose down |
| **Rudder** | Left stick right | Trailing edge RIGHT | Yaw nose right |
| **Rudder** | Left stick left | Trailing edge LEFT | Yaw nose left |

* Servo mechanics: a servo motor drives a plastic output arm to a precise angle based on a PWM (pulse-width modulation) signal from the receiver
* Pushrod: transfers servo arm motion to the control surface horn; must be rigid to avoid backlash and flex under load
* Control horn: lever arm on the control surface; the further from the hinge, the more mechanical advantage but less throw
* Hinge: must allow free rotation without friction — any binding reduces control authority and can lead to control surface flutter

|  |
| --- |
| **Why Control Direction Matters**  A reversed elevator is one of the most common causes of first-flight crashes in RC aviation.  When the pilot pushes forward to correct a nose-up attitude, a reversed elevator pitches the nose further up — into an unrecoverable stall.  All aircraft manufacturers verify control direction through a mandatory pre-flight check before every flight.  The verification sequence from Project 5 (Pre-Flight Checklist) is the standard solution to this problem. |

---

## 4.4 Rc Plane Wing

* Wing loading = Total Weight ÷ Wing Area. Units: g/cm² (model aircraft) or kg/m² (full-size aircraft)
* Stall speed increases with wing loading: to generate the same lift with more weight, the aircraft must fly faster
* Low wing loading: slow stall speed, forgiving handling, slow cruise — gliders, sailplanes, trainers
* High wing loading: fast stall speed, stable in turbulence, fast cruise — cargo aircraft, fighters, airliners

|  |
| --- |
| **Stall Speed Formula**  Stall speed increases with the square root of wing loading.  If wing loading doubles, stall speed increases by √2 ≈ 1.41 times.  Example: baseline stall speed 20 km/h; double the wing loading → stall speed = 28 km/h.  This is why heavily loaded cargo aircraft need much longer runways for takeoff and landing. |

---

## 4.5 Vtol Hybrid

**VTOL Configuration Comparison**

| **Configuration** | **Description** | **Pros** | **Cons** |
| --- | --- | --- | --- |
| **Quad-Plane** | Separate vertical lift motors + fixed-wing cruise motor | Simpler; well-supported in ArduPilot | More motors, more weight, more drag in cruise |
| **Tilt-Rotor** | Forward motors tilt from vertical to horizontal | Efficient in both modes; fewer motors | Complex mechanism; risk of tilt servo failure |
| **Tilt-Wing** | Entire wing section tilts with motors | Most aerodynamically efficient | Heaviest mechanism; most complex build |

**Flight Mode Descriptions**

| **Mode** | **Motor Orientation** | **Flight Behaviour** | **Control Source** |
| --- | --- | --- | --- |
| **Hover (VTOL)** | Vertical — lift motors up | Quadcopter-like; differential thrust for attitude | FC multirotor PID loop |
| **Transition** | Tilting / mixed | Both lift and wing lift acting; critical phase | FC transitions between control loops |
| **Forward Flight** | Horizontal — cruise motor forward | Fixed-wing; ailerons, elevator, rudder active | FC fixed-wing PID loop |

|  |
| --- |
| **The Transition Phase – Most Critical Design Challenge**  During transition, the aircraft must accelerate from hover speed (0 m/s) to minimum wing flying speed (typically 12–18 m/s).  The lift motors are gradually reducing power as wing lift builds — there is a critical phase where neither system is fully effective.  Too slow a transition: the aircraft loses altitude and may crash.  Too fast a transition: the aircraft pitches violently and may enter an unrecoverable attitude.  The transition airspeed parameter in ArduPilot controls exactly where this crossover happens. |

---

## 4.6 Autonomous Formation

**Formation Types**

| **Formation** | **Layout** | **Use Case** | **Offset (Leader = 0,0)** |
| --- | --- | --- | --- |
| **Line Astern** | Wingman directly behind leader | Simple; easy to implement | 0, –5 m |
| **V-Formation** | Leader at front; wingman each side | Survey; area coverage | –5 m left / +5 m right |
| **Echelon Right** | Wingman to right and behind | Camera covering left | –5 m, –5 m |
| **Box** | 2×2 grid | Maximum area coverage | ±5 m, ±5 m |

**Communication Data Fields**

| **Data Field** | **Update Rate** | **Format** | **Example** |
| --- | --- | --- | --- |
| **GPS Latitude** | 2 Hz | Decimal degrees | 5.560012 |
| **GPS Longitude** | 2 Hz | Decimal degrees | -0.205741 |
| **Altitude (m)** | 2 Hz | Metres above home | 12.5 |
| **Heading (°)** | 5 Hz | 0–360 magnetic | 274 |
| **Speed (m/s)** | 5 Hz | Ground speed | 8.2 |
| **Status flag** | 1 Hz | Integer (0=OK, 1=WARN) | 0 |

|  |
| --- |
| **Leader-Follower Control Loop**  Step 1: Leader broadcasts its GPS position, altitude, heading, and speed at 2 Hz.  Step 2: Wingman receives the data and applies the formation offset in the North-East frame.  Step 3: Wingman sends a GUIDED waypoint command to its own flight controller with the offset target.  Step 4: Wingman FC flies to the offset target using its own GPS.  Step 5: Loop repeats every 500 ms.  Key constraint: GPS accuracy is ±1–3 m, so the minimum achievable offset error is also ±1–3 m. |

---

## 4.7 Long Endurance

**Solar Power System Chain**

| **Component** | **Function** | **Efficiency** | **Key Selection Factor** |
| --- | --- | --- | --- |
| **Solar panel** | Harvests sunlight → DC electricity | 15–22% | W/g (power per gram of panel weight) |
| **MPPT controller** | Maximises panel power extraction | 90–97% | Match to panel voltage; low quiescent current |
| **Li-ion battery** | Stores excess solar energy | 95–99% (charge/discharge) | Energy density (Wh/g); cycle life |
| **ESC** | Controls motor speed | 95–98% | Current rating ≥ peak motor current |
| **Brushless motor** | Converts electrical energy to rotation | 70–85% | KV: low KV (< 800) for large efficient prop |
| **Propeller** | Converts rotation to thrust | 55–75% | Large diameter, low pitch, slow RPM |

|  |
| --- |
| **The Energy Balance Equation**  For sustained solar flight: P\_solar > P\_motor + P\_avionics  P\_solar (W) = Panel area (m²) × Solar irradiance (W/m²) × Panel efficiency × MPPT efficiency  At noon in Ghana: Solar irradiance ≈ 900–1000 W/m². A 200 cm² panel (0.02 m²) at 20% efficiency = 3.6–4.0 W.  A 400 g aircraft needs approximately 3 W to maintain level flight at 8 m/s.  Therefore, 200 cm² of panel is the theoretical minimum — in practice, aim for 250–300 cm² to allow for clouds and non-ideal angle. |

**Why Ghana is Ideal for Solar Aviation**

* Ghana lies within 10° of the equator — solar irradiance is among the highest in the world (900–1050 W/m² at noon)
* Minimal seasonal variation: solar panels produce consistently near peak output year-round
* This makes Ghana an excellent location for solar UAV operations, agricultural monitoring, and long-endurance surveillance
* The Ghana Meteorological Agency uses solar-powered weather stations — the same solar energy principles in this project

---

