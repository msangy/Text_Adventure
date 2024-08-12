#Copy of Text-Based Adventure Game from Code_Camp
#The Story

story = "You and a few teammates have just arrived on a new planet to do some scouting. You are all preparing to exit the spaceship and set up machinery outside when suddenly, you hear a hissing sound outside of the hatch. Alarm bells starting ringing! What do you do?: "

#Dictionaries (to add onto the story, add additional prompts and outcomes)
story_part_one = {
    "prompts": [
        "Press 'dress' to continue putting on your spacesuites and open the hatch to investigate.", 
        "Press 'investigate' to step back and head to the window to investigate: ",
    ],
    "outcomes": {
        "dress": "You and your teammates hurriedly finish putting on your spacesuits, the hissing sound growing louder with every passing second. With a quick nod to each other, you unlatch the hatch and cautiously step outside. The alien landscape is shrouded in a thin mist, and the source of the hissing becomes immediately clear—a nearby vent in the ship is releasing a stream of gas into the atmosphere. As you approach to inspect it, the ground suddenly trembles, and from beneath the earth, strange bioluminescent tendrils begin to emerge, reaching for your team. You have a split second to react.",
        "investigate": "You step away from the hatch, motioning for your teammates to follow as you all make your way to the nearest window. Peering out, you can barely make out the shape of something slithering just beyond the ship, partially obscured by the planet's fog. Suddenly, a large shadow moves across the ground, and you see it—a massive, serpent-like creature with glowing eyes, coiled around the ship. The hissing was not from the ship but from the creature itself! It seems to be resting now, but your presence might disturb it."
    }
}

story_part_two = {
    "prompts": [
        "Press 'retreat' to retreat back into the ship and seal the hatch.",
        "Press 'talk' to try and communicate with the creature using your ship’s external speakers: ",
    ],
    "outcomes": {
        "retreat": "You and your teammates dash back toward the hatch, slamming it shut just as the tendrils begin to slap against the door. The ship rocks violently as the alien tendrils attempt to breach the hull. You quickly check the control panel, realizing that the ship's integrity is holding for now, but the tendrils are starting to wrap around the landing gear, anchoring you to the ground. Your onboard AI alerts you that the power levels are draining rapidly due to the strain on the ship's systems. You need to make a decision quickly.",
        "talk": "You decide to take a chance and attempt communication with the creature. Activating the ship’s external speakers, you broadcast a series of harmonic tones, hoping to convey peaceful intentions. The creature's glowing eyes flicker as it reacts to the sounds, its body shifting slightly. For a moment, it seems to be listening. Then, in response, the creature emits a deep, resonant hum that reverberates through the ship. The vibrations cause the ship's systems to glitch momentarily, but the creature doesn’t attack."
    }
}

story_part_three = {
    "prompts": [
        "Press 'cut' to try and cut the power to the affected systems to conserve energy.",
        "Press 'engage' to engage the tendrils with your laser tools: ",
    ],
    "outcomes": {
        "cut": "You make the quick decision to cut power to non-essential systems, hoping to buy the ship some time. The lights dim, and the hum of the engines quiets to a whisper, but the tendrils continue to lash against the hull. Suddenly, the AI alerts you to an unexpected surge—something is hacking into the ship’s systems through the tendrils. You watch in horror as the controls begin to override themselves. The ship’s AI, usually calm and efficient, starts to glitch, displaying erratic messages on the screen. You realize that whatever is controlling the tendrils is now inside your ship’s systems.",
        "engage": "Without hesitation, you and your teammates activate your laser tools, slicing through the bioluminescent tendrils with precision. The tendrils retract, oozing a strange fluid, but more of them emerge from the ground, faster and more aggressive. As you fend them off, one of your teammates spots something glinting in the distance—an ancient structure partially buried under the planet's surface. The tendrils seem to be originating from that direction. It might be a control center or something more sinister, but it’s your only lead."
    }
}

#List of the stories so that we can iterate (add new dictionary names to the list below to continue story)
story_parts = [
    story_part_one,
    story_part_two,
    story_part_three
]

#Defined a function
def adventure(prompts, outcomes):
    for prompt in prompts:
        print(prompt)

    while True:
        choice = input(">>> ")
        outcome =outcomes.get(choice)
        if outcome:
            print(outcome)
            break
        else:
            print("Please enter one of: ", outcomes.keys())

print(story)
for story_part in story_parts:
    prompt = story_part["prompts"]
    outcomes = story_part["outcomes"]
    adventure(prompt,outcomes)


