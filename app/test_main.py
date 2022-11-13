from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)

# TODO: 
# WRITE TESTS: 
# - valid csv file upload on post "upload" endpoint
# - valid xlsx file upload ...
# - invalid csv file upload ...
# - invalid xlxs file upload ...


def test_get_synopsis_file_not_found():
  response = client.get("/airline/synopsis")
  assert response.status_code == 404
  

def test_get_synopsis():
    response = client.get("/airlines.xlsx/synopsis")
    assert response.status_code == 200
    assert response.json() == {
  "columns": [
    {
      "header": "airline_name",
      "type": "Text",
      "Sample": [
        "American Airlines",
        "Delta Air Lines",
        "Southwest Airlines",
        "United Airlines"
      ]
    },
    {
      "header": "date",
      "type": "Text",
      "Sample": [
        1512259200000000000,
        1512172800000000000,
        1506556800000000000,
        1506297600000000000,
        1504656000000000000
      ]
    },
    {
      "header": "score",
      "type": "Number",
      "Sample": [
        5,
        4,
        1,
        3,
        2
      ]
    },
    {
      "header": "title",
      "type": "Text",
      "Sample": [
        "Great non stop to Reagan-but have be bussed to and from terminal",
        "Best seat to Asia",
        "On time, and no delays",
        "Online Ticket Purchase Super Easy!",
        "Can't Give it a Minus Rating"
      ]
    },
    {
      "header": "location",
      "type": "Text",
      "Sample": [
        "Birmingham AL",
        "Birmingham, AL, USA",
        "Huntsville, Alabama",
        "Albertville, Alabama",
        "Knoxville, Tennessee"
      ]
    },
    {
      "header": "review",
      "type": "Text",
      "Sample": [
        "This is the only non stop to Reagan (DCA). Only complaint is with the arrival and departure. American Eagle flights park remotely on the tarmac at DCA and you are bussed to and from the terminal. Most carry on baggage is checked at the gate, so you are at the mercy of the weather. I have gotten frostbite, soaking wet, and a sunburn waiting for the bags at DCA. At BHM at least you have a jetway. I have since learned to pack an oversized handbag to squeeze under the seat",
        "My husband uses American for business travel and so this flight was on frequent flyer redemption. After checking seat guru, I choose the second row of economy on the aisle for my trip to Tokyo. I was lucky and the seat next to me was empty so there was more space to spread out. This seat had the benefits of bulkhead without the non-moveable armrest problem in bulkhead. Since I can't afford business class, this is the seat I will choose for an international flight every time. Lots of leg room and comfort.The meals were tasty and plentiful. Staff was courteous and helpful. Boarding process was smooth and uneventful. I enjoyed the trip to Japan very much. Good wifi connection if you purchased it and good selection of movies in on-board entertainment option. I used my own headphones.On the return trip, I chose the window seat thinking I could lean against the window to sleep on an overnight flight. Big mistake. It was a fuller flight and I was jammed in a corner, unable to sleep, but with two neighbors who were. I tend to try to be courteous, so I didn't want to repeatedly wake them so I could walk around. It was miserable. I will choose that aisle seat on that row every time from this point forward. I would rather be crawled over than do the crawling, and with the lack of seat in front of the aisle seat in this configuration, most of that crawling doesn't really impact the person in that aisle seat.",
        "Always enjoy flying American Airlines. Have not experienced any delays or cancelations the last 3 times I used them. Employees are friendly and helpful. will use them again when I fly in February.",
        "Bought my ticket online directly with American Airlines. Super easy, direct flight to Chicago reasonable price. Love the email reminders to check in day prior. Easy to get electronic boarding ticket, even make seating changes. Gate agents were a little preoccupied with personal business. Flight attendants were very customer friendly.",
        "Here i am on hold with American Airlines for the third plus hour and counting. I book travel and on the way in, they had a delay that meant I wouldn't make my connection [no big surprise here...]. I had paid for seat upgrades including First Class on the longest leg which i didn't get on the rebooking. I am told I should get a refund in two billing cycles. OK, now I am trying to check in for my return flight. My locator reference doesn't work. [I can, however, see my wife's details with it. I simply don't seem to exist. My guess is that the agent at the midway point mucked everything up. I went to her to see if there were upgrades available for my wife and I. She booked one of us but not both then tried to back it out. It took her 45 minutes to get us boarded - 10 minutes after the next to last people. Any bets on whether I can get on the plane that I am checking into??? This is SOP for American Airlines!!!"
      ]
    },
    {
      "header": "flight_type",
      "type": "Text",
      "Sample": [
        "Domestic",
        "International",
        "Caribbean",
        "Mexico",
        "Canada"
      ]
    },
    {
      "header": "flight_class",
      "type": "Text",
      "Sample": [
        "Economy",
        "First Class",
        "Business Class"
      ]
    },
    {
      "header": "flight",
      "type": "Text",
      "Sample": [
        "Birmingham - Washington DC",
        "Birmingham - Tokyo",
        "Birmingham - Las Vegas",
        "Birmingham - Chicago",
        "Birmingham - Minneapolis"
      ]
    },
    {
      "header": "seat_comfort",
      "type": "Number",
      "Sample": [
        3,
        4,
        1,
        2,
        5
      ]
    },
    {
      "header": "customer_service",
      "type": "Number",
      "Sample": [
        5,
        4,
        1,
        3,
        2
      ]
    },
    {
      "header": "cleanliness",
      "type": "Number",
      "Sample": [
        5,
        2,
        3,
        1,
        4
      ]
    },
    {
      "header": "food_beverages",
      "type": "Number",
      "Sample": [
        3,
        2,
        1,
        4,
        5
      ]
    },
    {
      "header": "legroom",
      "type": "Number",
      "Sample": [
        3,
        5,
        2,
        1,
        4
      ]
    },
    {
      "header": "check_in",
      "type": "Number",
      "Sample": [
        4,
        1,
        3,
        5,
        2
      ]
    },
    {
      "header": "entertainment",
      "type": "Number",
      "Sample": [
        1,
        3,
        4,
        5,
        2
      ]
    },
    {
      "header": "nps",
      "type": "Number",
      "Sample": [
        10,
        7,
        8,
        2,
        3
      ]
    },
    {
      "header": "csat",
      "type": "Number",
      "Sample": [
        8,
        7,
        1,
        2,
        6
      ]
    },
    {
      "header": "nps_duplicate",
      "type": "Number",
      "Sample": [
        0
      ]
    },
    {
      "header": "ticket_price",
      "type": "Number",
      "Sample": [
        86,
        1336,
        68,
        604,
        87
      ]
    },
    {
      "header": "question",
      "type": "Text",
      "Sample": [
        "What went well?",
        "Other comments",
        "What can we improve?"
      ]
    },
    {
      "header": "sensitive",
      "type": "Number",
      "Sample": [
        0,
        1
      ]
    },
    {
      "header": "unique_id",
      "type": "Text",
      "Sample": [
        "jklf1pe2yh",
        "ezpe6o1rd2",
        "oxyv9mp41l",
        "hndb983xz5",
        "jhfchvz87q"
      ]
    },
    {
      "header": "departure_city",
      "type": "Text",
      "Sample": [
        "Birmingham",
        "Huntsville",
        "Mobile",
        "Dothan",
        "Anchorage"
      ]
    },
    {
      "header": "arrival_city",
      "type": "Text",
      "Sample": [
        "Washington DC",
        "Tokyo",
        "Las Vegas",
        "Chicago",
        "Minneapolis"
      ]
    },
    {
      "header": "departure_state",
      "type": "Text",
      "Sample": [
        " Alabama",
        " Alaska",
        " Antigua",
        " Argentina",
        " Arizona"
      ]
    },
    {
      "header": "arrival_state",
      "type": "Text",
      "Sample": [
        " District of Columbia",
        " Japan",
        " Nevada",
        " Illinois",
        " Minnesota"
      ]
    }
  ]
}