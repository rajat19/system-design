---
layout: post
title: "Design a Parking Lot"
author: "Rajat Srivastava"
categories: case_study
tags: [design]
image: parking/page.jpg
---

A parking lot or car park is a dedicated cleared area that is intended for parking vehicles. In most countries where cars are a major mode of transportation, parking lots are a feature of every city and suburban area. Shopping malls, sports stadiums, megachurches, and similar venues often feature parking lots over large areas.

<!-- 1. [System Requirements](#system-requirements)
- [System Requirements](#system-requirements)
- [Use Case Diagrams](#use-case-diagrams)
- [Class Diagrams](#class-diagrams)
- [Activity diagrams](#activity-diagrams)
- [Code](#code) -->

---
## System Requirements
We will focus on the following set of requirements while designing the parking lot:
1. The parking lot should have multiple floors where customers can park their cars.
2. The parking lot should have multiple entry and exit points.
3. Customers can collect a parking ticket from the entry points and can pay the parking fee at the exit points on their way out.
4. Customers can pay the tickets at the automated exit panel or to the parking attendant.
5. Customers can pay via both cash and credit cards.
6. Customers should also be able to pay the parking fee at the customer’s info portal on each floor. If the customer has paid at the info portal, they don’t have to pay at the exit.
7. The system should not allow more vehicles than the maximum capacity of the parking lot. If the parking is full, the system should be able to show a message at the entrance panel and on the parking display board on the ground floor.
8. Each parking floor will have many parking spots. The system should support multiple types of parking spots such as Compact, Large, Handicapped, Motorcycle, etc.
9. The Parking lot should have some parking spots specified for electric cars. These spots should have an electric panel through which customers can pay and charge their vehicles.
10. The system should support parking for different types of vehicles like car, truck, van, motorcycle, etc.
11. Each parking floor should have a display board showing any free parking spot for each spot type.
12. The system should support a per-hour parking fee model. For example, customers have to pay $4 for the first hour, $3.5 for the second and third hours, and $2.5 for all the remaining hours.

---
## Use Case Diagrams
Here are the main Actors in our system:

- **Admin:** Mainly responsible for adding and modifying parking floors, parking spots, entrance, and exit panels, adding/removing parking attendants, etc.
- **Customer:** All customers can get a parking ticket and pay for it.
- **Parking attendant:** Parking attendants can do all the activities on the customer’s behalf, and can take cash for ticket payment.
- **System:** To display messages on different info panels, as well as assigning and removing a vehicle from a parking spot.

Here are the top use cases for Parking Lot:

- **Add/Remove/Edit parking floor:** To add, remove or modify a parking floor from the system. Each floor can have its own display board to show free parking spots.
- **Add/Remove/Edit parking spot:** To add, remove or modify a parking spot on a parking floor.
- **Add/Remove a parking attendant:** To add or remove a parking attendant from the system.
- **Take ticket:** To provide customers with a new parking ticket when entering the parking lot.
- **Scan ticket:** To scan a ticket to find out the total charge.
- **Credit card payment:** To pay the ticket fee with credit card.
- **Cash payment:** To pay the parking ticket through cash.
- **Add/Modify parking rate:** To allow admin to add or modify the hourly parking rate.

![Use Case]({{ site.github.url }}/assets/img/parking/use-case.svg)

---
## Class Diagrams
Here are the main classes of our Parking Lot System:

- **ParkingLot:** The central part of the organization for which this software has been designed. It has attributes like ‘Name’ to distinguish it from any other parking lots and ‘Address’ to define its location.
- **ParkingFloor:** The parking lot will have many parking floors.
- **ParkingSpot:** Each parking floor will have many parking spots. Our system will support different parking spots 1) Handicapped, 2) Compact, 3) Large, 4) Motorcycle, and 5) Electric.
- **Account:** We will have two types of accounts in the system: one for an Admin, and the other for a parking attendant.
- **Parking ticket:** This class will encapsulate a parking ticket. Customers will take a ticket when they enter the parking lot.
- **Vehicle:** Vehicles will be parked in the parking spots. Our system will support different types of vehicles 1) Car, 2) Truck, 3) Electric, 4) Van and 5) Motorcycle.
- **EntrancePanel and ExitPanel:** EntrancePanel will print tickets, and ExitPanel will facilitate payment of the ticket fee.
- **Payment:** This class will be responsible for making payments. The system will support credit card and cash transactions.
- **ParkingRate:** This class will keep track of the hourly parking rates. It will specify a dollar amount for each hour. For example, for a two hour parking ticket, this class will define the cost for the first and the second hour.
- **ParkingDisplayBoard:** Each parking floor will have a display board to show available parking spots for each spot type. This class will be responsible for displaying the latest availability of free parking spots to the customers.
- **ParkingAttendantPortal:** This class will encapsulate all the operations that an attendant can perform, like scanning tickets and processing payments.
- **CustomerInfoPortal:** This class will encapsulate the info portal that customers use to pay for the parking ticket. Once paid, the info portal will update the ticket to keep track of the payment.
- **ElectricPanel:** Customers will use the electric panels to pay and charge their electric vehicles.

![Class Diagram]({{ site.github.url }}/assets/img/parking/class-diagram.png)

![UML Conventions]({{ site.github.url }}/assets/img/parking/uml.svg)

---
## Activity diagrams

- **Customer paying for parking ticket:** Any customer can perform this activity. Here are the set of steps:
![Activity Checkout]({{ site.github.url }}/assets/img/parking/activity-paying.svg)

---
## Code
Following is the skeleton code for our parking lot system:

- **Enums and Constants:** Here are the required enums, data types, and constants:
<div class="code-tab">
  <button class="code-tablinks" onclick="openCode(event, 'enumsJava')" type="button">Java</button>
  <button class="code-tablinks" onclick="openCode(event, 'enumsPy')" type="button">Python</button>
</div>

<!-- Tab content -->
<div id="enumsJava" class="code-tabcontent">
{% highlight java %}
public enum VehicleType {
  CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE
}

public enum ParkingSpotType {
  HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC
}

public enum AccountStatus {
  ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN
}

public enum ParkingTicketStatus {
  ACTIVE, PAID, LOST
}

public class Address {
  private String streetAddress;
  private String city;
  private String state;
  private String zipCode;
  private String country;
}

public class Person {
  private String name;
  private Address address;
  private String email;
  private String phone;
}
{% endhighlight %}
</div>

<div id="enumsPy" class="code-tabcontent">
{% highlight py %}
class VehicleType(Enum):
  CAR, TRUCK, ELECTRIC, VAN, MOTORBIKE = 1, 2, 3, 4, 5


class ParkingSpotType(Enum):
  HANDICAPPED, COMPACT, LARGE, MOTORBIKE, ELECTRIC = 1, 2, 3, 4, 5


class AccountStatus(Enum):
  ACTIVE, BLOCKED, BANNED, COMPROMISED, ARCHIVED, UNKNOWN = 1, 2, 3, 4, 5, 6


class ParkingTicketStatus(Enum):
  ACTIVE, PAID, LOST = 1, 2, 3


class Address:
  def __init__(self, street, city, state, zip_code, country):
    self.__street_address = street
    self.__city = city
    self.__state = state
    self.__zip_code = zip_code
    self.__country = country


class Person():
  def __init__(self, name, address, email, phone):
    self.__name = name
    self.__address = address
    self.__email = email
    self.__phone = phone
{% endhighlight %}
</div>

- **Account, Admin, and ParkingAttendant:** These classes represent various people that interact with our system:
<div class="code-tab">
  <button class="code-tablinks" onclick="openCode(event, 'accountsJava')">Java</button>
  <button class="code-tablinks" onclick="openCode(event, 'accountsPy')">Python</button>
</div>

<!-- Tab content -->
<div id="accountsJava" class="code-tabcontent">

{% highlight java %}
/// For simplicity, we are not defining getter and setter functions. The reader can
// assume that all class attributes are private and accessed through their respective
// public getter methods and modified only through their public methods function.

public abstract class Account {
  private String userName;
  private String password;
  private AccountStatus status;
  private Person person;

  public boolean resetPassword();
}

public class Admin extends Account {
  public bool addParkingFloor(ParkingFloor floor);
  public bool addParkingSpot(String floorName, ParkingSpot spot);
  public bool addParkingDisplayBoard(String floorName, ParkingDisplayBoard displayBoard);
  public bool addCustomerInfoPanel(String floorName, CustomerInfoPanel infoPanel);

  public bool addEntrancePanel(EntrancePanel entrancePanel);
  public bool addExitPanel(ExitPanel exitPanel);
}

public class ParkingAttendant extends Account {
  public bool processTicket(string TicketNumber);
}
{% endhighlight %}
</div>

<div id="accountsPy" class="code-tabcontent">
{% highlight py %}
class Account:
  def __init__(self, user_name, password, person, status=AccountStatus.Active):
    self.__user_name = user_name
    self.__password = password
    self.__person = person
    self.__status = status

  def reset_password(self):
    None


class Admin(Account):
  def __init__(self, user_name, password, person, status=AccountStatus.Active):
    super().__init__(user_name, password, person, status)

  def add_parking_floor(self, floor):
    None

  def add_parking_spot(self, floor_name, spot):
    None

  def add_parking_display_board(self, floor_name, display_board):
    None

  def add_customer_info_panel(self, floor_name, info_panel):
    None

  def add_entrance_panel(self, entrance_panel):
    None

  def add_exit_panel(self, exit_panel):
    None


class ParkingAttendant(Account):
  def __init__(self, user_name, password, person, status=AccountStatus.Active):
    super().__init__(user_name, password, person, status)

  def process_ticket(self, ticket_number):
    None
{% endhighlight %}
</div>

- **ParkingSpot:** Here is the definition of ParkingSpot and all of its children classes:
<div class="code-tab">
  <button class="code-tablinks" onclick="openCode(event, 'spotJava')">Java</button>
  <button class="code-tablinks" onclick="openCode(event, 'spotPy')">Python</button>
</div>

<!-- Tab content -->
<div id="spotJava" class="code-tabcontent">
{% highlight java %}
public abstract class ParkingSpot {
  private String number;
  private boolean free;
  private Vehicle vehicle;
  private final ParkingSpotType type;

  public boolean IsFree();

  public ParkingSpot(ParkingSpotType type) {
    this.type = type;
  }

  public boolean assignVehicle(Vehicle vehicle) {
    this.vehicle = vehicle;
    free = false;
  }

  public boolean removeVehicle() {
    this.vehicle = null;
    free = true;
  }
}

public class HandicappedSpot extends ParkingSpot {
  public HandicappedSpot() {
    super(ParkingSpotType.HANDICAPPED);
  }
}

public class CompactSpot extends ParkingSpot {
  public CompactSpot() {
    super(ParkingSpotType.COMPACT);
  }
}

public class LargeSpot extends ParkingSpot {
  public LargeSpot() {
    super(ParkingSpotType.LARGE);
  }
}

public class MotorbikeSpot extends ParkingSpot {
  public MotorbikeSpot() {
    super(ParkingSpotType.MOTORBIKE);
  }
}

public class ElectricSpot extends ParkingSpot {
  public ElectricSpot() {
    super(ParkingSpotType.ELECTRIC);
  }
}
{% endhighlight %}
</div>

<div id="spotPy" class="code-tabcontent">
{% highlight py %}
class ParkingSpot(ABC):
  def __init__(self, number, parking_spot_type):
    self.__number = number
    self.__free = True
    self.__vehicle = None
    self.__parking_spot_type = parking_spot_type

  def is_free(self):
    return self.__free

  def assign_vehicle(self, vehicle):
    self.__vehicle = vehicle
    free = False

  def remove_vehicle(self):
    self.__vehicle = None
    free = True


class HandicappedSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.HANDICAPPED)


class CompactSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.COMPACT)


class LargeSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.LARGE)


class MotorbikeSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.MOTORBIKE)


class ElectricSpot(ParkingSpot):
  def __init__(self, number):
    super().__init__(number, ParkingSpotType.ELECTRIC)
{% endhighlight %}
</div>

- **Vehicle:** Here is the definition for Vehicle and all of its child classes:
<div class="code-tab">
  <button class="code-tablinks" onclick="openCode(event, 'vehicleJava')">Java</button>
  <button class="code-tablinks" onclick="openCode(event, 'vehiclePy')">Python</button>
</div>

<!-- Tab content -->
<div id="vehicleJava" class="code-tabcontent">
{% highlight java %}
public abstract class Vehicle {
  private String licenseNumber;
  private final VehicleType type;
  private ParkingTicket ticket;

  public Vehicle(VehicleType type) {
    this.type = type;
  }

  public void assignTicket(ParkingTicket ticket) {
    this.ticket = ticket;
  }
}

public class Car extends Vehicle {
  public Car() {
    super(VehicleType.CAR);
  }
}

public class Van extends Vehicle {
  public Van() {
    super(VehicleType.VAN);
  }
}

public class Truck extends Vehicle {
  public Truck() {
    super(VehicleType.TRUCK);
  }
}

// Similarly we can define classes for Motorcycle and Electric vehicles
{% endhighlight %}
</div>

<div id="vehiclePy" class="code-tabcontent">
{% highlight py %}
from abc import ABC, abstractmethod

class Vehicle(ABC):
  def __init__(self, license_number, vehicle_type, ticket=None):
    self.__license_number = license_number
    self.__type = vehicle_type
    self.__ticket = ticket

  def assign_ticket(self, ticket):
    self.__ticket = ticket


class Car(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.CAR, ticket)


class Van(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.VAN, ticket)


class Truck(Vehicle):
  def __init__(self, license_number, ticket=None):
    super().__init__(license_number, VehicleType.TRUCK, ticket)
"""
Similarly we can define classes for Motorcycle and Electric vehicles
"""
{% endhighlight %}
</div>

- **ParkingFloor:** This class encapsulates a parking floor:

<div class="code-tab">
  <button class="code-tablinks" onclick="openCode(event, 'floorJava')">Java</button>
  <button class="code-tablinks" onclick="openCode(event, 'floorPy')">Python</button>
</div>

<!-- Tab content -->
<div id="floorJava" class="code-tabcontent">
{% highlight java %}
public class ParkingFloor {
  private String name;
  private HashMap<String, HandicappedSpot> handicappedSpots;
  private HashMap<String, CompactSpot> compactSpots;
  private HashMap<String, LargeSpot> largeSpots;
  private HashMap<String, MotorbikeSpot> motorbikeSpots;
  private HashMap<String, ElectricSpot> electricSpots;
  private HashMap<String, CustomerInfoPortal> infoPortals;
  private ParkingDisplayBoard displayBoard;

  public ParkingFloor(String name) {
    this.name = name;
  }

  public void addParkingSpot(ParkingSpot spot) {
    switch (spot.getType()) {
    case ParkingSpotType.HANDICAPPED:
      handicappedSpots.put(spot.getNumber(), spot);
      break;
    case ParkingSpotType.COMPACT:
      compactSpots.put(spot.getNumber(), spot);
      break;
    case ParkingSpotType.LARGE:
      largeSpots.put(spot.getNumber(), spot);
      break;
    case ParkingSpotType.MOTORBIKE:
      motorbikeSpots.put(spot.getNumber(), spot);
      break;
    case ParkingSpotType.ELECTRIC:
      electricSpots.put(spot.getNumber(), spot);
      break;
    default:
      print("Wrong parking spot type!");
    }
  }

  public void assignVehicleToSpot(Vehicle vehicle, ParkingSpot spot) {
    spot.assignVehicle(vehicle);
    switch (spot.getType()) {
    case ParkingSpotType.HANDICAPPED:
      updateDisplayBoardForHandicapped(spot);
      break;
    case ParkingSpotType.COMPACT:
      updateDisplayBoardForCompact(spot);
      break;
    case ParkingSpotType.LARGE:
      updateDisplayBoardForLarge(spot);
      break;
    case ParkingSpotType.MOTORBIKE:
      updateDisplayBoardForMotorbike(spot);
      break;
    case ParkingSpotType.ELECTRIC:
      updateDisplayBoardForElectric(spot);
      break;
    default:
      print("Wrong parking spot type!");
    }
  }

  private void updateDisplayBoardForHandicapped(ParkingSpot spot) {
    if (this.displayBoard.getHandicappedFreeSpot().getNumber() == spot.getNumber()) {
      // find another free handicapped parking and assign to displayBoard
      for (String key : handicappedSpots.keySet()) {
        if (handicappedSpots.get(key).isFree()) {
          this.displayBoard.setHandicappedFreeSpot(handicappedSpots.get(key));
        }
      }
      this.displayBoard.showEmptySpotNumber();
    }
  }

  private void updateDisplayBoardForCompact(ParkingSpot spot) {
    if (this.displayBoard.getCompactFreeSpot().getNumber() == spot.getNumber()) {
      // find another free compact parking and assign to displayBoard
      for (String key : compactSpots.keySet()) {
        if (compactSpots.get(key).isFree()) {
          this.displayBoard.setCompactFreeSpot(compactSpots.get(key));
        }
      }
      this.displayBoard.showEmptySpotNumber();
    }
  }

  public void freeSpot(ParkingSpot spot) {
    spot.removeVehicle();
    switch (spot.getType()) {
    case ParkingSpotType.HANDICAPPED:
      freeHandicappedSpotCount++;
      break;
    case ParkingSpotType.COMPACT:
      freeCompactSpotCount++;
      break;
    case ParkingSpotType.LARGE:
      freeLargeSpotCount++;
      break;
    case ParkingSpotType.MOTORBIKE:
      freeMotorbikeSpotCount++;
      break;
    case ParkingSpotType.ELECTRIC:
      freeElectricSpotCount++;
      break;
    default:
      print("Wrong parking spot type!");
    }
  }
}
{% endhighlight %}
</div>

<div id="floorPy" class="code-tabcontent">
{% highlight py %}
class ParkingFloor:
  def __init__(self, name):
    self.__name = name
    self.__handicapped_spots = {}
    self.__compact_spots = {}
    self.__large_spots = {}
    self.__motorbike_spots = {}
    self.__electric_spots = {}
    self.__info_portals = {}
    self.__display_board = ParkingDisplayBoard()

  def add_parking_spot(self, spot):
    switcher = {
      ParkingSpotType.HANDICAPPED: self.__handicapped_spots.put(spot.get_number(), spot),
      ParkingSpotType.COMPACT: __compact_spots.put(spot.get_number(), spot),
      ParkingSpotType.LARGE: __large_spots.put(spot.get_number(), spot),
      ParkingSpotType.MOTORBIKE: __motorbike_spots.put(spot.get_number(), spot),
      ParkingSpotType.ELECTRIC: __electric_spots.put(spot.get_number(), spot),
    }
    switcher.get(spot.get_type(), 'Wrong parking spot type')

  def assign_vehicleToSpot(self, vehicle, spot):
    spot.assign_vehicle(vehicle)
    switcher = {
      ParkingSpotType.HANDICAPPED: self.update_display_board_for_handicapped(spot),
      ParkingSpotType.COMPACT: self.update_display_board_for_compact(spot),
      ParkingSpotType.LARGE: self.update_display_board_for_large(spot),
      ParkingSpotType.MOTORBIKE: self.update_display_board_for_motorbike(spot),
      ParkingSpotType.ELECTRIC: self.update_display_board_for_electric(spot),
    }
    switcher(spot.get_type(), 'Wrong parking spot type!')

  def update_display_board_for_handicapped(self, spot):
    if self.__display_board.get_handicapped_free_spot().get_number() == spot.get_number():
      # find another free handicapped parking and assign to display_board
      for key in self.__handicapped_spots:
        if self.__handicapped_spots.get(key).is_free():
          self.__display_board.set_handicapped_free_spot(
            self.__handicapped_spots.get(key))

      self.__display_board.show_empty_spot_number()

  def update_display_board_for_compact(self, spot):
    if self.__display_board.get_compact_free_spot().get_number() == spot.get_number():
      # find another free compact parking and assign to display_board
      for key in self.__compact_spots.key_set():
        if self.__compact_spots.get(key).is_free():
          self.__display_board.set_compact_free_spot(
            self.__compact_spots.get(key))

      self.__display_board.show_empty_spot_number()

  def free_spot(self, spot):
    spot.remove_vehicle()
    switcher = {
      ParkingSpotType.HANDICAPPED: self.__free_handicapped_spot_count += 1,
      ParkingSpotType.COMPACT: self.__free_compact_spot_count += 1,
      ParkingSpotType.LARGE: self.__free_large_spot_count += 1,
      ParkingSpotType.MOTORBIKE: self.__free_motorbike_spot_count += 1,
      ParkingSpotType.ELECTRIC: self.__free_electric_spot_count += 1,
    }

    switcher(spot.get_type(), 'Wrong parking spot type!')
{% endhighlight %}
</div>

- **ParkingDisplayBoard:** This class encapsulates a parking display board:

<div class="code-tab">
  <button class="code-tablinks" onclick="openCode(event, 'displayJava')">Java</button>
  <button class="code-tablinks" onclick="openCode(event, 'displayPy')">Python</button>
</div>

<!-- Tab content -->
<div id="displayJava" class="code-tabcontent">
{% highlight java %}
public class ParkingDisplayBoard {
  private String id;
  private HandicappedSpot handicappedFreeSpot;
  private CompactSpot compactFreeSpot;
  private LargeSpot largeFreeSpot;
  private MotorbikeSpot motorbikeFreeSpot;
  private ElectricSpot electricFreeSpot;

  public void showEmptySpotNumber() {
    String message = "";
    if(handicappedFreeSpot.IsFree()){
      message += "Free Handicapped: " + handicappedFreeSpot.getNumber();
    } else {
      message += "Handicapped is full";
    }
    message += System.lineSeparator();

    if(compactFreeSpot.IsFree()){
      message += "Free Compact: " + compactFreeSpot.getNumber();
    } else {
      message += "Compact is full";
    }
    message += System.lineSeparator();

    if(largeFreeSpot.IsFree()){
      message += "Free Large: " + largeFreeSpot.getNumber();
    } else {
      message += "Large is full";
    }
    message += System.lineSeparator();

    if(motorbikeFreeSpot.IsFree()){
      message += "Free Motorbike: " + motorbikeFreeSpot.getNumber();
    } else {
      message += "Motorbike is full";
    }
    message += System.lineSeparator();

    if(electricFreeSpot.IsFree()){
      message += "Free Electric: " + electricFreeSpot.getNumber();
    } else {
      message += "Electric is full";
    }

    Show(message);
  }
}
{% endhighlight %}
</div>

<div id="displayPy" class="code-tabcontent">
{% highlight py %}
class ParkingDisplayBoard:
  def __init__(self, id):
    self.__id = id
    self.__handicapped_free_spot = None
    self.__compact_free_spot = None
    self.__large_free_spot = None
    self.__motorbike_free_spot = None
    self.__electric_free_spot = None

  def show_empty_spot_number(self):
    message = ""
    if self.__handicapped_free_spot.is_free():
      message += "Free Handicapped: " + self.__handicapped_free_spot.get_number()
    else:
      message += "Handicapped is full"
    message += "\n"

    if self.__compact_free_spot.is_free():
      message += "Free Compact: " + self.__compact_free_spot.get_number()
    else:
      message += "Compact is full"
    message += "\n"

    if self.__large_free_spot.is_free():
      message += "Free Large: " + self.__large_free_spot.get_number()
    else:
      message += "Large is full"
    message += "\n"

    if self.__motorbike_free_spot.is_free():
      message += "Free Motorbike: " + self.__motorbike_free_spot.get_number()
    else:
      message += "Motorbike is full"
    message += "\n"

    if self.__electric_free_spot.is_free():
      message += "Free Electric: " + self.__electric_free_spot.get_number()
    else:
      message += "Electric is full"

    print(message)
{% endhighlight %}
</div>

- **ParkingLot:** Our system will have only one object of this class. This can be enforced by using the [Singleton](https://en.wikipedia.org/wiki/Singleton_pattern) pattern. In software engineering, the singleton pattern is a software design pattern that restricts the instantiation of a class to only one object.

<div class="code-tab">
  <button class="code-tablinks" onclick="openCode(event, 'lotJava')">Java</button>
  <button class="code-tablinks" onclick="openCode(event, 'lotPy')">Python</button>
</div>

<!-- Tab content -->
<div id="lotJava" class="code-tabcontent">
{% highlight java %}
public class ParkingLot {
  private String name;
  private Location address;
  private ParkingRate parkingRate;

  private int compactSpotCount;
  private int largeSpotCount;
  private int motorbikeSpotCount;
  private int electricSpotCount;
  private final int maxCompactCount;
  private final int maxLargeCount;
  private final int maxMotorbikeCount;
  private final int maxElectricCount;

  private HashMap<String, EntrancePanel> entrancePanels;
  private HashMap<String, ExitPanel> exitPanels;
  private HashMap<String, ParkingFloor> parkingFloors;

  // all active parking tickets, identified by their ticketNumber
  private HashMap<String, ParkingTicket> activeTickets;

  // singleton ParkingLot to ensure only one object of ParkingLot in the system,
  // all entrance panels will use this object to create new parking ticket: getNewParkingTicket(),
  // similarly exit panels will also use this object to close parking tickets
  private static ParkingLot parkingLot = null;

  // private constructor to restrict for singleton
  private ParkingLot() {
    // 1. initialize variables: read name, address and parkingRate from database
    // 2. initialize parking floors: read the parking floor map from database,
    //  this map should tell how many parking spots are there on each floor. This
    //  should also initialize max spot counts too.
    // 3. initialize parking spot counts by reading all active tickets from database
    // 4. initialize entrance and exit panels: read from database
  }

  // static method to get the singleton instance of StockExchange
  public static ParkingLot getInstance() {
    if (parkingLot == null) {
      parkingLot = new ParkingLot();
    }
    return parkingLot;
  }

  // note that the following method is 'synchronized' to allow multiple entrances
  // panels to issue a new parking ticket without interfering with each other
  public synchronized ParkingTicket getNewParkingTicket(Vehicle vehicle) throws ParkingFullException {
    if (this.isFull(vehicle.getType())) {
      throw new ParkingFullException();
    }
    ParkingTicket ticket = new ParkingTicket();
    vehicle.assignTicket(ticket);
    ticket.saveInDB();
    // if the ticket is successfully saved in the database, we can increment the parking spot count
    this.incrementSpotCount(vehicle.getType());
    this.activeTickets.put(ticket.getTicketNumber(), ticket);
    return ticket;
  }

  public boolean isFull(VehicleType type) {
    // trucks and vans can only be parked in LargeSpot
    if (type == VehicleType.Truck || type == VehicleType.Van) {
      return largeSpotCount >= maxLargeCount;
    }

    // motorbikes can only be parked at motorbike spots
    if (type == VehicleType.Motorbike) {
      return motorbikeSpotCount >= maxMotorbikeCount;
    }

    // cars can be parked at compact or large spots
    if (type == VehicleType.Car) {
      return (compactSpotCount + largeSpotCount) >= (maxCompactCount + maxLargeCount);
    }

    // electric car can be parked at compact, large or electric spots
    return (compactSpotCount + largeSpotCount + electricSpotCount) >= (maxCompactCount + maxLargeCount
        + maxElectricCount);
  }

  // increment the parking spot count based on the vehicle type
  private boolean incrementSpotCount(VehicleType type) {
    if (type == VehicleType.Truck || type == VehicleType.Van) {
      largeSpotCount++;
    } else if (type == VehicleType.Motorbike) {
      motorbikeSpotCount++;
    } else if (type == VehicleType.Car) {
      if (compactSpotCount < maxCompactCount) {
        compactSpotCount++;
      } else {
        largeSpotCount++;
      }
    } else { // electric car
      if (electricSpotCount < maxElectricCount) {
        electricSpotCount++;
      } else if (compactSpotCount < maxCompactCount) {
        compactSpotCount++;
      } else {
        largeSpotCount++;
      }
    }
  }

  public boolean isFull() {
    for (String key : parkingFloors.keySet()) {
      if (!parkingFloors.get(key).isFull()) {
        return false;
      }
    }
    return true;
  }

  public void addParkingFloor(ParkingFloor floor) {
    /* store in database */ }

  public void addEntrancePanel(EntrancePanel entrancePanel) {
    /* store in database */ }

  public void addExitPanel(ExitPanel exitPanel) {
    /* store in database */ }
}
{% endhighlight %}
</div>

<div id="lotPy" class="code-tabcontent">
{% highlight py %}
import threading

class ParkingLot:
  # singleton ParkingLot to ensure only one object of ParkingLot in the system,
  # all entrance panels will use this object to create new parking ticket: get_new_parking_ticket(),
  # similarly exit panels will also use this object to close parking tickets
  instance = None

  class __OnlyOne:
    def __init__(self, name, address):
      # 1. initialize variables: read name, address and parking_rate from database
      # 2. initialize parking floors: read the parking floor map from database,
      #    this map should tell how many parking spots are there on each floor. This
      #    should also initialize max spot counts too.
      # 3. initialize parking spot counts by reading all active tickets from database
      # 4. initialize entrance and exit panels: read from database

      self.__name = name
      self.__address = address
      self.__parking_rate = ParkingRate()

      self.__compact_spot_count = 0
      self.__large_spot_count = 0
      self.__motorbike_spot_count = 0
      self.__electric_spot_count = 0
      self.__max_compact_count = 0
      self.__max_large_count = 0
      self.__max_motorbike_count = 0
      self.__max_electric_count = 0

      self.__entrance_panels = {}
      self.__exit_panels = {}
      self.__parking_floors = {}

      # all active parking tickets, identified by their ticket_number
      self.__active_tickets = {}

      self.__lock = threading.Lock()

  def __init__(self, name, address):
    if not ParkingLot.instance:
      ParkingLot.instance = ParkingLot.__OnlyOne(name, address)
    else:
      ParkingLot.instance.__name = name
      ParkingLot.instance.__address = address

  def __getattr__(self, name):
    return getattr(self.instance, name)

  def get_new_parking_ticket(self, vehicle):
    if self.is_full(vehicle.get_type()):
      raise Exception('Parking full!')
    # synchronizing to allow multiple entrances panels to issue a new
    # parking ticket without interfering with each other
    self.__lock.acquire()
    ticket = ParkingTicket()
    vehicle.assign_ticket(ticket)
    ticket.save_in_DB()
    # if the ticket is successfully saved in the database, we can increment the parking spot count
    self.__increment_spot_count(vehicle.get_type())
    self.__active_tickets.put(ticket.get_ticket_number(), ticket)
    self.__lock.release()
    return ticket

  def is_full(self, type):
    # trucks and vans can only be parked in LargeSpot
    if type == VehicleType.Truck or type == VehicleType.Van:
      return self.__large_spot_count >= self.__max_large_count

    # motorbikes can only be parked at motorbike spots
    if type == VehicleType.Motorbike:
      return self.__motorbike_spot_count >= self.__max_motorbike_count

    # cars can be parked at compact or large spots
    if type == VehicleType.Car:
      return (self.__compact_spot_count + self.__large_spot_count) >= (self.__max_compact_count + self.__max_large_count)

    # electric car can be parked at compact, large or electric spots
    return (self.__compact_spot_count + self.__large_spot_count + self.__electric_spot_count) >= (self.__max_compact_count + self.__max_large_count
                                                                                                  + self.__max_electric_count)

  # increment the parking spot count based on the vehicle type
  def increment_spot_count(self, type):
    if type == VehicleType.Truck or type == VehicleType.Van:
      large_spot_count += 1
    elif type == VehicleType.Motorbike:
      motorbike_spot_count += 1
    elif type == VehicleType.Car:
      if self.__compact_spot_count < self.__max_compact_count:
        compact_spot_count += 1
      else:
        large_spot_count += 1
    else:  # electric car
      if self.__electric_spot_count < self.__max_electric_count:
        electric_spot_count += 1
      elif self.__compact_spot_count < self.__max_compact_count:
        compact_spot_count += 1
      else:
        large_spot_count += 1

  def is_full(self):
    for key in self.__parking_floors:
      if not self.__parking_floors.get(key).is_full():
        return False
    return True

  def add_parking_floor(self, floor):
    # store in database
    None

  def add_entrance_panel(self, entrance_panel):
    # store in database
    None

  def add_exit_panel(self,  exit_panel):
    # store in database
    None
{% endhighlight %}
</div>