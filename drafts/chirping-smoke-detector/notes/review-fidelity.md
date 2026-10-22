# Smoke Detectors That Chirp: fidelity review

Checked `drafts/chirping-smoke-detector/guide.md`, version 0.5.0, against `notes/sources.md` (no raw
pages kept). The hype notes were not read. Sources fetched 22 October 2026.

| Verdict | Count |
|---|---|
| Wrong | 2 |
| Overreach | 8 |
| Unsourced | 1 |
| Naming | 2 |
| Non-public | 0 |
| Stale | 0 |

Each verdict section runs from most to least serious. Replacements are the same length as the
original or shorter.

## Wrong

### W1. CO alarm action drops "call 9-1-1" and "stay out" (line 146, What does the sound mean?)

**Guide:** "| Four beeps repeating on a combination alarm | Carbon monoxide | Go outside and call for help. |"

**Source** (NFPA, Learn the Sounds, content.nfpa.org/-/media/Project/Storefront/Catalog/Files/Fire-Prevention-Week/2024/FPW24-Learn-the-Sounds.pdf): "A continuous set of four loud beeps—beep, beep, beep, beep—means carbon monoxide is present in your home. Go outside, call 9-1-1 and stay out."

**Verdict:** wrong. The source gives a specific action: call 9-1-1 and stay out. "Call for help" is vague and leaves out "stay out", which is the step that keeps people from going back into the CO.

**Corrected:** "| Four beeps repeating on a combination alarm | Carbon monoxide | Go out, call 9-1-1, stay out. |"

### W2. Battery change is a minimum, not a fixed interval (line 84, Battery)

**Guide:** "A battery powers the smoke alarm, or backs up a hardwired one. Change it once a year."

**Source** (NFPA, Educational Messages Desk Reference 2026, www.nfpa.org/-/media/project/storefront/catalog/files/home-fire-safety/emac/educationalmessagesdeskreference.pdf): "If your smoke alarm uses replaceable batteries, change the batteries at least once a year." USFA (www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/): "Replace the backup battery at least once every year."

**Verdict:** wrong (minor). Both sources say "at least" once a year. The guide states a fixed interval.

**Corrected:** "A battery runs a smoke alarm or backs up a hardwired one. Change it at least yearly."

## Overreach

### O1. Reset leaves out the breaker on hardwired alarms and is one brand's procedure (line 85, Battery)

**Guide:** "A new battery usually stops the chirp. If it doesn’t, hold the test button for at least 15 seconds with the battery out, then put it back."

**Source** (Kidde, What Causes Intermittent Beeping or Chirping?, www.kidde.com/support/smoke-alarms/intermittent-beeping-causes): "Turn off the power to the smoke alarm at the circuit breaker. Remove the smoke alarm from the mounting bracket and disconnect the power. Remove the battery. Press and hold the test button for at least 15 seconds." First Alert SM110V-AC (support.firstalert.com/sfc/servlet.shepherd/document/download/069Vs00000REeCbIAL): "Turn off the power to the area where the Alarm is installed before removing it from the mounting bracket. Failure to turn off the power first may result in serious electrical shock, injury or death."

**Verdict:** overreach, and a safety gap. The 15-second reset is Kidde's procedure; First Alert's comparable step is 5 to 10 seconds and is not described as a chirp reset. For hardwired alarms Kidde turns off the breaker first, and the guide doesn't say so here. Sealed-battery alarms have no battery to take out.

**Corrected:** "A new battery usually stops the chirp. If not, many models reset: breaker off, battery out, hold test 15 seconds, then restore both."

### O2. Same reset gap in the sounds table (line 144, What does the sound mean?)

**Guide:** "Clear the fault with the battery out, then replace the smoke alarm if it still chirps."

**Source** (Kidde, What Causes Intermittent Beeping or Chirping?, www.kidde.com/support/smoke-alarms/intermittent-beeping-causes): "Turn off the power to the smoke alarm at the circuit breaker. … Remove the battery. Press and hold the test button for at least 15 seconds."

**Verdict:** overreach, and a safety gap. As O1: the hardwired procedure starts with the breaker, and the step is model-specific.

**Corrected:** "Reset it (breaker off first if hardwired). If it still chirps, replace it."

### O3. "There’s no fire" (line 13, Why is my smoke alarm chirping?)

**Guide:** "One short chirp every 30 to 60 seconds or so means a smoke alarm wants attention, and there’s no fire."

**Source** (Kidde, What Causes Consistent Chirping?, www.kidde.com/support/smoke-alarms/consistent-chirping-causes): "Hush Condition – If your alarm has the Hush feature, the alarm will chirp every 30-40 seconds for approximately seven minutes while the Hush feature is activated." NFPA (Desk Reference): "A single “chirp” every 30 or 60 seconds means the battery is low and must be changed."

**Verdict:** overreach. The sources say what a chirp signals, not that there is no fire. A hushed alarm chirps after it has sensed smoke, and a chirping alarm with a fault may not sense a fire at all.

**Corrected:** "One short chirp every 30 to 60 seconds means a smoke alarm wants attention, not that there’s a fire."

### O4. End of life stated as certain after a new battery (line 13, Why is my smoke alarm chirping?)

**Guide:** "If a new battery doesn’t stop it, the smoke alarm is at the end of its life."

**Source** (Kidde, What Causes Intermittent Beeping or Chirping?, www.kidde.com/support/smoke-alarms/intermittent-beeping-causes): "Sometimes, the alarm’s processor retains error conditions, such as a weak battery, even after the battery is replaced."

**Verdict:** overreach. NFPA says this, but Kidde gives a stored fault as another cause, and the guide itself offers a reset on lines 85 and 144. Line 13 should match those lines.

**Corrected:** "If a new battery and a reset don’t stop it, replace the smoke alarm."

### O5. The chirp "will be back" (line 45, Chirp)

**Guide:** "A chirp that stops by morning will be back the next night. Change the battery anyway."

**Source** (Kidde, Why Do Smoke Alarms Always Chirp in the Middle of the Night?, www.kidde.com/support/smoke-alarms/nighttime-alarm-chirps): "That’s why the alarm may sound a low-battery chirp in the middle of the night, and then stop when the home warms up a few degrees."

**Verdict:** overreach. The source says "may"; no source says the chirp returns the next night.

**Corrected:** "A chirp that stops by morning can return the next night. Change the battery anyway."

### O6. The odd light is "usually" the one to fix (line 65, Indicator light)

**Guide:** "When you can’t place the chirp, compare the lights. The odd one out is usually the one to fix."

**Source** (First Alert, SM110V-AC manual, support.firstalert.com/sfc/servlet.shepherd/document/download/069Vs00000REeCbIAL): "This feature is designed to help you identify which Alarm needs to have the battery replaced." Kidde i12040A (sources.md, "Not stated"): no LED pattern that marks the low-battery unit.

**Verdict:** overreach. Only one source has a low-battery light pattern; the Kidde i12040A has none. An odd light can also be alarm memory (Kidde i12040A, First Alert P1210). Line 32 already says "may".

**Corrected:** "When you can’t place the chirp, compare the lights. The odd one out may be the one to fix."

### O7. A hush always buys a night’s sleep (line 105, Hush button)

**Guide:** "A hush buys you a night’s sleep and fixes nothing. The chirp comes back."

**Source** (First Alert, SM210M manual, support.firstalert.com/sfc/servlet.shepherd/document/download/069Vs00000REkZkIAL): "This Silence Feature can temporarily quiet the Low Battery Warning “chirp”." (no duration given). Kidde 20SD10 guide (brand.kidde.com/m/46fc0720d3d7e5d4/original/UG_DETECT_5in_DC_EN.pdf): "Note: 7 days after Low Battery begins, the notifications cannot be silenced."

**Verdict:** overreach. Low-battery silence runs 8, 13 or 24 hours on the models in the sources, one manual gives no duration, and one model stops allowing it after 7 days. Line 104 says "on many models"; line 105 drops the hedge.

**Corrected:** "A hush may buy a night’s sleep but fixes nothing. The chirp comes back."

### O8. "A battery wears out much sooner" (line 137, Manufacture date)

**Guide:** "The manufacture date never changes. A battery wears out much sooner."

**Source** (USFA, Smoke alarms, www.usfa.fema.gov/prevention/home-fires/prepare-for-fire/smoke-alarms/): "a nonreplaceable 10-year lithium-ion (“long-life”) battery".

**Verdict:** overreach. True for replaceable batteries only. A sealed battery lasts as long as the alarm, as line 97 says.

**Corrected:** "The date never changes. A replaceable battery wears out much sooner."

## Unsourced

### U1. Only the problem alarm chirps (line 27, Which one is it?)

**Guide:** "A chirp is hard to place by ear. Usually only the smoke alarm with the problem chirps, so use your eyes as well."

**Verdict:** unsourced. sources.md says "No source states outright that only the unit with the problem chirps", and Kidde warns of "an echoing chirp from one unit to the next" on interconnected alarms. A source would need to say that interconnected alarms don't share the trouble chirp. Either find one and add it to `sources.md`, or cut the claim. What the sources do support is the light (First Alert SM110V-AC low battery latch).

**Corrected:** "A chirp is hard to place by ear. The one with the problem may blink differently, so use your eyes as well."

## Naming

### N1. First Alert calls it Silence, not Hush (line 103, Hush button)

**Guide:** "A button on the cover, often the test button too."

**Source** (First Alert, P1210 manual, support.firstalert.com/sfc/servlet.shepherd/document/download/0694x00000PlZpgAAF): "Low battery silence: The Alarm can be silenced for 8 hours." SM110V-AC: "Test/Silence button". Kidde i12040A: "Test/Hush button".

**Verdict:** naming. "Hush" is Kidde’s word. First Alert owners will look for a button marked Silence.

**Corrected:** "A button marked Hush or Silence, often Test too."

### N2. Manuals say LED (line 20, terms table)

**Guide:** "| Indicator light | The small light whose blinking shows the smoke alarm’s condition. |"

**Source** (Kidde i12040A guide, brand.kidde.com/m/79d343435488dfc/original/Product_UG_i12040A-i12080A-User-Guide_En.pdf): "Standby Condition: The red LED will flash every 40 seconds". First Alert SM110V-AC: "the Smoke/Power LED flashes Green".

**Verdict:** naming. Every manual in the sources says LED. Line 148 sends readers to the manual, so they need the word.

**Corrected:** "| Indicator light | The small light (LED) whose blinking shows the alarm’s condition. |"

## Non-public

None. All sources are public manufacturer, NFPA or USFA pages.

## Stale

None. The Kidde i12040A guide (2015) and the Learn the Sounds handout (©2021) are old, but the guide uses them only for model facts ("on some models") or for advice that NFPA repeats in its 2026 edition.

## Safety order (not a fidelity verdict)

- **Line 34:** "Take that smoke alarm down and read the date on the back. If it’s hardwired, turn off its breaker first." The facts match SM110V-AC and Kidde, but the breaker comes after the instruction to take the alarm down. Someone acting step by step could start before reading the second sentence. Corrected: "If hardwired, turn off its breaker. Then take that smoke alarm down and read the date on the back."
- **Line 37 against lines 85 and 144:** "Never take out the battery" is followed by a reset done "with the battery out". The sources forbid removing the battery to stop an alarm, not taking it out briefly for a reset. If O1 and O2 are applied ("then restore both"), the conflict is smaller. Readers may still need "and leave it out" on line 37, but that is a call for the reader panel.

## Sources page

- Listed but not used: none. All seven listed sources back at least one line.
- Used but not listed:
  - **Kidde, Smoke and Combination Smoke/CO Alarms User Guide, 20SDR/20SD10 family** (brand.kidde.com/m/46fc0720d3d7e5d4/original/UG_DETECT_5in_DC_EN.pdf). It is the only source for AA batteries (line 83, "A 9-volt or AA battery") and for a 24-hour low-battery hush (line 104, "some hours").
  - **First Alert, User’s Manual, Model P1210** (support.firstalert.com/sfc/servlet.shepherd/document/download/0694x00000PlZpgAAF). It backs the 8-hour low-battery silence and 9-minute nuisance silence (line 104, "a few minutes", "On many models … some hours"), and "when one chirps, replace the smoke alarm" for sealed units (line 97). Without it and the 20SD10 guide, "many models" rests on one listed manual.
  - **Kidde, What Causes Consistent Chirping?** (www.kidde.com/support/smoke-alarms/consistent-chirping-causes). It is the only source for "Replace the battery, then press test" (line 143: "Replace the battery when this occurs, then test your alarm") and for the 7-minute Hush (line 104).
  - Optional: **First Alert, User’s Manual, Model SM210M** (support.firstalert.com/sfc/servlet.shepherd/document/download/069Vs00000REkZkIAL) also backs the 9-minute nuisance silence.
