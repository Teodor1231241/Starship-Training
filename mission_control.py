import importlib.util
import os

ALL_MODULES = [
    ("weapons",    "Tactical Weapons"),
    ("shields",    "Deflector Shields"),
    ("thrusters",  "Sublight Thrusters"),
    ("scanner",    "Deep-Space Scanner"),
    ("ai_core",    "Ship AI Computer"),
    ("warp_drive", "Hyperdrive Core")
]

print("\n" + "=" * 68)
print("   U.S.S. PYCHARM (STARSHIP-3416) - MAIN BRIDGE TERMINAL   ")
print("=" * 68)

installed_count = 0
total_ship_power = 0
battle_events = []

print("\n[SYSTEM DIAGNOSTICS - SCANNING 6 MODULE SLOTS...]")
print("-" * 68)

for mod_file, label in ALL_MODULES:
    filename = f"{mod_file}.py"
    if os.path.exists(filename):
        spec = importlib.util.spec_from_file_location(mod_file, filename)
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            sys_name = getattr(module, "system_name", "Custom Module")
            power = int(getattr(module, "power_rating", 75))
            action = getattr(module, "action_text", "activates at full power!")

            installed_count += 1
            total_ship_power += power
            status = f"[ONLINE - {power:3d} PWR]"
            print(f" [OK] {label:19} | {status:18} | {sys_name}")
            battle_events.append(f" -> [{label.upper()}] {sys_name} {action}")
        except Exception as e:
            print(f" [!!] {label:19} | [ERROR IN CODE]    | Check {filename}: {e}")
    else:
        total_ship_power += 10
        print(f" [XX] {label:19} | [OFFLINE - 10 PWR] | Backup mode ({filename} missing)")

print("-" * 68)
print(f" MODULES INSTALLED: {installed_count}/6  |  TOTAL SHIP POWER: {total_ship_power} / 250 needed")
print("=" * 68)

print("\nRED ALERT! ALIEN DREADNOUGHT DETECTED IN SECTOR 3416!")
if battle_events:
    print("Engaging student-engineered systems:\n")
    for event in battle_events:
        print(event)
else:
    print(" -> No student modules installed yet! Relying on rusty backup systems...")

print("\n" + "-" * 68)
if total_ship_power >= 450:
    print(" MISSION VICTORY! Your 3 custom modules overpowered the Alien Dreadnought!")
    print(" The galaxy is safe thanks to the engineering crew of Classroom 3416!")
elif total_ship_power >= 130:
    print(" PARTIAL SUCCESS! The ship survived, but we need more student")
    print(" modules merged into 'main' to reach 250 Power and defeat the boss!")
else:
    print(" HULL CRITICAL! The ship is running on offline backup systems (60 PWR)!")
    print(" Merge 3 student modules into 'main' to reach 250+ Power!")
print("=" * 68 + "\n")
