companies = "Coursera, Google, Facebook, Amazon, Microsoft, Airbnb, Uber, Twilio, Stripe, Twitter, Paypal, Cisco, Yelp, Meraki, Addepar, GoDaddy, LiveRamp, FiveStars, Asana, Square, Blizzard, Indeed, eBay, Fitbit, Pure Storage, Qualtrics, Quantcast, Whitepages, Bloomberg, Affirm, Tubular Labs, Recruit Holdings (Tokyo), Delphix, Doordash, Quora, Ciena, TubeMogul, Capital One, Wish, Slack, Tinder, Medallia, Blue Apron, JP Morgan Technology Analyst, Grand Rounds, Visa, Lattice Engines, Segment, Blend Labs, Moody's, AT&T, Lob, EA, IBM, Demandware, Curalate, Pixar, Xero, Viasat, Qualcomm, Samsung"

companies_list = companies.split(", ")

with open("links.txt", "w+") as f:
	for company in companies_list:
		search = "http://www.google.com/search?hl=en&q=" + '+'.join(company.split(" ")) +"+new+grad+software+engineer"
		f.write(search)
		f.write("\n")
