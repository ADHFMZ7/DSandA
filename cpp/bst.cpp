#include <iostream>

int main(){
  





}

class Node{
public:
  Node(int data){}
  *Node left, right;


  void insert(int data){
    if (data >= this.data){
      if (this.right == NULL){
        this.right = new Node(data);
      }
      else{this.right.insert(data)}

    }
    else if (data < this.data)

  }
}
