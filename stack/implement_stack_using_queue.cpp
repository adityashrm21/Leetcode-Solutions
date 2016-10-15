class Stack {
public:
    // Push element x onto stack.
    queue<int> q1, q2;
    
    void push(int x) {
        
        while(!q1.empty())
        {
            int top=q1.front();
            q2.push(top);
            q1.pop();
        }
        
        q1.push(x);
        
        while(!q2.empty())
        {
            int top=q2.front();
            q1.push(top);
            q2.pop();
        }
        
        
    }

    // Removes the element on top of the stack.
    void pop() {
        
        q1.pop();
        
    }

    // Get the top element.
    int top() {
        
        return q1.front();
        
    }

    // Return whether the stack is empty.
    bool empty() {
        
        if(q1.empty()) return true;
        
        return false;
    }
};