



taco_places = [
    {
        "name": "Los Burritos Tapatio",
        "recommend": "Al Pastor Taco",
        "score": 10,
        "comments": "🔥 Suburb gem! Absolute favorite Al Pastor.",
    },
    {
        "name": "Birria Zaragoza",
        "recommend": "Goat Taco",
        "score": 9,
        "comments": "Goat taco is unbeatable — authentic and perfect. 🌟 Deducted 1 point because they sell out fast and close too early (7 PM on weekdays).",
    },
    {
        "name": "Angela's Burrito",
        "recommend": "Al Pastor Taco",
        "score": 10,
        "comments": "🌆 A great alternative to Tapatio if you're in the city!",
    },
    {
        "name": "El Tragon",
        "recommend": "Quesabirria",
        "score": 8,
        "comments": "Still good! But I preferred Angela's and Tapatio's Al Pastor, so I'd say more like a 9/10. ⏰ Deducted 1 point because they close early (8 PM weekdays, 4 PM Saturday, closed Sunday).",
    },
    {
        "name": "Jaimito's Burritos",
        "recommend": "🌶️ Try the grilled jalapeños! Salsa is good.",
        "score": 8,
        "comments": "Friendly staff — he told me to ask for grilled jalapeños next time before they run out, so he gave me extra green salsa 😄. It's close to my place and open late. Al Pastor reminds me of El Tragon — not the best, not the worst. I would've given a 7, but added 1 point for convenience.",
    },
    {
        "name": "Jorge Taco y Burrito House",
        "recommend": "🥤 Horchata, maybe?",
        "score": 6,
        "comments": "Tried the lunch special beef tacos... turned out to be ground beef (not asada steak like I expected — but hey, they didn’t lie). Al Pastor marinade was too overpowering. Horchata was actually good! 📍 It’s right next to my work (CML), so I added 1 point for convenience.",
    },
]

#sort highest score 

sorted_places = sorted(taco_places, key=lambda x: x["score"], reverse=True)


print("🌮 Taco Places in Chicago - Ranked by Me!\n")
for i, place in enumerate(sorted_places, start=1):
    print(f"{i}. {place['name']} ({place['score']}/10)")
    print(f"   ⭐ Recommend: {place['recommend']}")
    print(f"   📝 Comments: {place['comments']}\n")



