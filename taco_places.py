# taco_places.py

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
        "score": 10,
        "comments": "Goat taco is unbeatable. Authentic & perfect.",
    },
    {
        "name": "Angela's Burrito",
        "recommend": "Al Pastor Taco",
        "score": 10,
        "comments": "Great alternative to Tapatio if you’re in the city.",
    },
    {
        "name": "El Tragon",
        "recommend": "Quesabirria",
        "score": 8,
        "comments": "Still good! But I preferred Angela's and Tapatio's Al Pastor.",
    },
]

#sort highest score 

sorted_places = sorted(taco_places, key=lambda x: x["score"], reverse=True)


print("🌮 Taco Places in Chicago - Ranked by Me!\n")
for i, place in enumerate(sorted_places, start=1):
    print(f"{i}. {place['name']} ({place['score']}/10)")
    print(f"   ⭐ Recommend: {place['recommend']}")
    print(f"   📝 Comments: {place['comments']}\n")



