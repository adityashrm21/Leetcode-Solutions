class MinStack {
public:
    /** initialize your data structure here. */
    
    stack<int> elementStack;
    stack<int> minimumStack;
    int minElement = -1;

    MinStack() {
        
        while(!elementStack.empty())
        elementStack.pop();

        while(!minimumStack.empty())
        minimumStack.pop();
        minElement = -1;
    }

    void push(int x) {
        elementStack.push(x);
        if(elementStack.size() == 1 || x <= minElement) {
            minimumStack.push(x);
            minElement = x;
        }
    }

    void pop() {
        
        if(!elementStack.empty())
        {
            if (elementStack.top() == minElement) {
                minimumStack.pop();
                if (!minimumStack.empty()) {
                    minElement = minimumStack.top();
                } else {
                    minElement = -1;
                }
            }
            
            elementStack.pop();
        }
    }       

    int top() {
        if (elementStack.empty()) return -1;
        return elementStack.top();
    }

    int getMin() {
        return minElement;
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(x);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */