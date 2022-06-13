

template <typename T>
class Vector {

public:
  
  int default_capacity = 64;

  Vector(int capacity = default_capacity) {
    
    size_ = 0;
    setCapacity(capacity);

  }

  void append(T element) {
      
  }



private:
  
  int size_;
  int capacity_;
  T* list_;

  void setCapacity(int capacity) {
    T* temp = new T[capacity];
    for (int i = 0; i < size_; i++) {
      temp[i] = list_[i];
    }
    delete [] list_;
    list_ = temp;
    temp = nullptr;
    capacity_ = capacity;
  }

};
