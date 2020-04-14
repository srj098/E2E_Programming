class LinkedLists {
  head: ListNode;

  addFirst(data: number): void {
    if(!this.head){
      this.head = new ListNode(data);
      this.head.next = null;
    } else {
      let newNode = new ListNode(data);
      newNode.next = this.head;
      this.head = newNode;
    }
  };

  addLast(data: number): void {
    if(!this.head){
      this.head = new ListNode(data);
    } else {
        if(this.head.next == null){
          let newNode = new ListNode(data);
          this.head.next = newNode;
        } else {
            while(this.head.next !== null){
              let nextNode = this.head.next;
              this.head = nextNode;
            }
            let newNode = new ListNode(data);
            this.head = newNode;              
        }        
    }
  };

  removeFirst(): void {
    if(!this.head){
      throw new Error("nothing to delete");
    } else {
       if(this.head.next == null){
          this.head = null;
        } else {
            let nextNode = this.head.next;
            this.head = nextNode;
        }
    }
  }

  removeLast(): void {
    if(!this.head){
      throw new Error("nothing to delete");
    } else {
        if(this.head.next == null){
          this.head = null;
        } else {
            let previousNode: ListNode;
            while(this.head.next !== null){
                previousNode = this.head;
                let nextNode = this.head.next;
                this.head = nextNode;
              }
            this.head = previousNode;
            this.head.next = null;
          }
      }
  }

}

class ListNode {
  public data: number;
  public next: ListNode;

  constructor(data: number){
    this.data = data;
  }
}

const linkedList = new LinkedLists();

linkedList.addFirst(1);
linkedList.addFirst(2);
linkedList.addFirst(3);

linkedList.removeFirst();
linkedList.removeLast();

console.log(linkedList);
