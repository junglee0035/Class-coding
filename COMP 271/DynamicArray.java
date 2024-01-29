/**
 * An object with dynamic storage capability for Strings.
 * Desired behavior:
 * - Detect when full and size up by a given factor;
 * - Capable of reporting how much much data store;
 * - index addressable (random access)
 * - a contains method
 * - data to be added to the end of existing data
 * - ability to delete data and re-compact the storage
 */
public class DynamicArray {

  /** Constant with array default size */
  private static final int DEFAULT_SIZE = 2;

  /** Resize factor for enlarging a full array */
  private static final int RESIZE_FACTOR = 2;

  /** Underlying array with strings to store */
  private String[] data;

  /** Next available position to accept data */
  private int nextAvailable;

  /** Basic constructor */
  public DynamicArray(int size) {
    // Make sure size is a legit value
    if (size < 1)
      size = DEFAULT_SIZE;
    this.data = new String[size];
    this.nextAvailable = 0;
  } // basic constructor

  /** Default constructor */
  public DynamicArray() {
    // Call basic constructor with size = DEFAULT_SIZE
    this(DEFAULT_SIZE);
  } // default constructor

  /**
   * Method to add a string to the object
   * 
   * @param string String to add to the object's underying array
   */
  public void add(String string) {
    // If array is full resize first then add String to underlying array
    if (this.nextAvailable == this.data.length) {
      resize();
    }
    this.data[this.nextAvailable] = string;
    // Advance to the next available position
    nextAvailable++;
  } // method add

  /**
   * Method to resize the array when full
   */
  private void resize() {
    // Create a larger array
    String[] temp = new String[RESIZE_FACTOR*this.data.length];
    // copy strings from current array to larger array
    for (int i = 0; i < this.data.length; i++) {
      temp[i] = this.data[i];
    }
    // Replace underlying array with the new larger array
    this.data = temp;
  } // method resize

  /**
   * Retrieve an element by location index.
   *
   * @param index int with the position of element we want to retrieve
   * @return the string an positiion [index] or null if position is invalind or empty
   */
  public String retrieve(int index) {
    String retrieved = null;
    if (index >= 0 && index < this.nextAvailable) {
      retrieved = this.data[index];
    }
    return retrieved;
  } // method retrieve

  /**
   * Remove an element by location index and rearrange the remaining elements
   * to fill the gap.
   *
   * @param index int with the position of element we want to retrieve
   * @return the string an positiion [index] or null if position is invalind or empty
   */
  public String remove(int index) {
    String removed = this.retrieve(index);
    if (removed != null) {
      for (int i = index; i < this.nextAvailable-1; i++) {
        this.data[i] = this.data[i+1];
      }
    }
    return removed;
  } // method retrieve

  public int indexOf(String targetString) {
    for (int i = 0; i < this.nextAvailable; i++) {
        if (this.data[i] != null && this.data[i].equals(targetString)) {
            return i;
        }
    }
    return -1; 
  }
  public int count(String string) {
    int counter = 0;
    for (int i = 0; i < this.nextAvailable; i++) {
      if (this.data[i].equals(string)) {
        counter++;
      }
    }
    return counter;
  }
  public void insert(int where, String what) {
    // First check if position is legit
    if (where >= 0 && where < this.nextAvailable) {
      // position legit; is array full?
      if (this.nextAvailable == this.data.length) {
        resize();
      }
      // Room assured.
      for (int i = this.nextAvailable; i != where; i--) {
        this.data[i] = this.data[i - 1];
      }
      // Shifting complete. Overwrite position [where]
      this.data[where] = what;
    }
    this.nextAvailable++;
  } // method insert
  
  public String removeFront() {
    return this.remove(0);
  }

  public void addFront(String string) {
    this.insert(0, string);
  }
  
  public String removeLast() {
    return this.remove(this.nextAvailable - 1);
  }
  
  public void addUnique(String string) {
    if (this.contains(string)) {
      this.add(string);
    }
  }

  public boolean contains(String string) {
    for (int i = 0; i< this.nextAvailable; i++) {
      if (this.data[i] != null && this.data[i].equals(string)) {
        return true;
      }
    }
    return false;
  }
} // class DynamicArray