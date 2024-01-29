/**
 * A class that simulates a train line by linking train station objects
 * together. The class uses two train station objects to define a train
 * line: its first station and its last station. New stations are added
 * always at the end of the line, and that's why it's important to know
 * where the last station is.
 */
public class TrainLine {

  /** Constant with message for string representation of an empty line */
  private static final String EMPTY_LINE = "This train line has no stations.";

  /**
   * The first station in the train line. This field is significant because
   * it provides us with a starting point for traversing the train line in
   * search of a particular station or for other purposes when traversal is
   * necessary.
   */
  private TrainStation first;

  /**
   * The last station in the train line. This field is significant because it
   * allows us to add new stations at the end of the line, superfase.
   */
  private TrainStation last;

  /**
   * Number of stations in a line. Neeeded for Comparable.
   */
  private int numberOfStations;

  /**
   * Default constructor. Sets both first and last stations to null.
   */
  public TrainLine() {
    this.first = null;
    this.last = null;
    this.numberOfStations = 0;
  } // default constructor

  /**
   * Add a train station at the back of the train line. The new station
   * will become the last station in the line.
   *
   * @param name String with name of new station to add.
   */
  public void addStation(String name) {
    // Create the new train station to add
    TrainStation newStation = new TrainStation(name);
    this.numberOfStations++;
    // Determine where to add the new train station
    if (this.first == null) {
      // Train line is empty: this is the first station we add
      this.first = newStation;
    } else {
      // Train line not empty: new station goes after last station
      this.last.setNext(newStation);
    }
    // Update the last station to the newly added station
    this.last = newStation;
  } // method addStation

  /**
   * Overloaded method addStation to take a TrainStation object as param.
   */
  public void addStation(TrainStation trainStation) {
    if (this.first == null) {
      this.first = trainStation;
    } else {
      this.last.setNext(trainStation);
    }
    this.last = trainStation;
  } // method addStation

  /**
   * Determine if a train station with a given name exists in the train line.
   *
   * @param name String with name of train station to search the train line for
   * @return true if train station with given name exists in line,
   *         false, otherwise.
   */
  public boolean contains(String name) {
    // Assume station doesn't exist
    boolean found = false;
    // Search only if line is not empty
    if (this.first != null) {
      // Line not empty; proceed with search starting from first station
      TrainStation cursor = this.first;
      // Explore every station until we exit the train line by arriving
      // at the null that the last station points to or until we find a
      // station with the given name.
      while (cursor != null && !found) {
        // Check if current station (where the cursor is) matches the name
        found = cursor.getName().equals(name);
        // Proceed to the next station
        cursor = cursor.getNext();
      }
    }
    return found;
  } // method contains

  /**
   * Find the middle station in the train line
   *
   * @return TrainStation that is at the middle of the line. If the line has
   *         an even number of train stations, the first of the two mid-
   *         stations is returned. If the line is empty, return null.
   */
  public TrainStation findMiddle() {
    // Prepare a null object to return (in case line is empty)
    TrainStation middle = null;
    // Make sure train line is not empty
    if (this.first != null) {
      // Use two pointers to traverse train line from beginning.
      // Slow traverses one station at a time.
      // Fast traverses skips a station and goes to the one after that
      TrainStation slow = this.first;
      TrainStation fast = this.first;
      // Traverse as long as fast pointer has somewhere to go
      while (fast.hasNext() && fast.getNext().hasNext()) {
        // Fast goes to its next stations' next station
        fast = fast.getNext().getNext();
        // Slow goes to its next station
        slow = slow.getNext();
      }
      // When the loop ends, slow is the middle station
      middle = slow;

    }
    return middle;
  } // method findMiddle

  /**
   * Determines if a TrainLine has an infinite loop. That usually happens when
   * the last station points to an existing station object and not to null.
   * If there is a loop, two pointers traveling at twice the speed of each other
   * will eventually coincide at the same station.
   * 
   * @ return true if line has a loop; false if no loop or line is empty
   */
  public boolean hasLoop() {
    // Assume there is no loop
    boolean loop = false;
    // Guard against empty line
    if (this.first != null) {
      // Set slow and fast pointers at the beginning of the line
      TrainStation slow = this.first;
      TrainStation fast = this.first;
      // While loop ends when not safe to advance fast pointer or when loop found
      while (!loop && fast.hasNext() && fast.getNext().hasNext()) {
        fast = fast.getNext().getNext();
        slow = slow.getNext();
        loop = fast == slow;
      }
    }
    return loop;
  } // method hasLoop

  /**
   * Finds the sequence position of a station in a line.
   *
   * return -1 if no station with given name or line is empty, 0 or greater
   * with the sequence position of the station otherwise.
   */
  public int indexOf(String name) {
    // Assume no station here
    int index = -1;
    // Guard against empty line
    if (this.first != null) {
      // Start search from beginning
      TrainStation cursor = this.first;
      // Sequency counter
      int i = 0;
      // Search until loop not -1 or until end of line
      while (cursor != null && index < 0) {
        // If station found, assign sequence counter to loop
        index = (cursor.getName().equals(name)) ? i : index;
        i++;
        cursor = cursor.getNext();
      }
    }
    return index;
  } // method indexOf


  /**
   * Deletes a TrainStation object from the TrainLine.
   */
  public void removeStation(String name) {
    // Empty line guard statement
    if (this.first != null) {
      // Check if station to delete is first station
      if (this.first.getName().equals(name)) {
        //Move first to its next, even if null. (first=null means empt line)
        this.first = this.first.getNext();
        // Did we just delete the only station in the line?
        if (this.first == null) {
          this.last = this.first; // last must also be null
        }
        // Revise number of stations in the TrainLine
        this.numberOfStations--;
      } else {
        // We are not deleting the first station. Go down the line to find
        // the station prior to the one we want delete
        boolean found = false;
        TrainStation cursor = this.first;
        while (!found && cursor.hasNext()) {
          found = cursor.getNext().getName().equals(name);
          cursor = (found) ? cursor : cursor.getNext();
        }
        // Loop stops either because we got to the end of the TrainLine and did
        // not find the station we want to delete, or because we found it.
        // Which of the two is the case?
        if (found) {
          // We have a station to delete; revise number of stations
          this.numberOfStations--;
          // Is it the last station?
          if (cursor.getNext() == this.last) {
            // delete last station
            cursor.setNext(null);
            // Make station prior to last, the new last station
            this.last = cursor;
          } else {
            // Delete station that is not the last, nor the first
            cursor.setNext(cursor.getNext().getNext());
          }
        }
      }
    } // guard if against empty TrainLine 
  } // method deleteStation

  
  /** 
   * Implements the Comparable interface by establishing a natural order for
   * TrainLine objects using the number of stations they have
   */
  public int compareTo(TrainLine other) {
    return this.numberOfStations - other.numberOfStations;
  } // method compareTo

  /**
   * String representation of the train line object, demonstrating the use
   * of StringBuilder.
   */
  public String toString() {
    StringBuilder sb = new StringBuilder();
    if (this.first == null) {
      // Line is empty
      sb.append(EMPTY_LINE);
    } else {
      // Line not empty, traverse and print its stations
      TrainStation current = this.first;
      while (current != null) {
        sb.append(String.format("\n%s", current.getName()));
        current = current.getNext();
      }
    }
    return sb.toString();
  } // method toString

  public boolean insert(String afterName, String newName) {
    //Flag to indicate if station was inserted
    boolean insertionSuccessful = false;
    
    //check if the trainline is not empty
    if (this.first != null) {
      //Initializes the cursor to the first station
      TrainStation cursor = this.first;

      //Search for existing station after new station should be inserted
      while (cursor != null && (cursor.getName() == null || !cursor.getName().equals(afterName))) {
            cursor = cursor.getNext();
      }
      // If the existing station is found, insert the new station
      if (cursor != null) {
        // Create the new station to insert
        TrainStation newStation = new TrainStation(newName);

        // Insert the new station after the existing station
        newStation.setNext(cursor.getNext());
        cursor.setNext(newStation);

        // If the existing station is also the last station, update the last station
        if (cursor == this.last) {
          this.last = newStation;
        }
        // Update the number of stations
        this.numberOfStations++;
        
        // Set the flag to indicate successful insertion
        insertionSuccessful = true;
      }
    }
    return insertionSuccessful;
  } //method insert
} // class TrainLine