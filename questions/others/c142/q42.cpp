# https://www.youtube.com/watch?v=K5nbi0CECjA
# https://leetcode-cn.com/problems/brace-expansion-ii/


public vector<string> beaceExpansion2(sting S){
    string s;
    for(int i =0; i < S.size();i++){
        if(isalpha(s[i])){
            s.push_back('{');
            s.push_back(s[i]);
            s.push_back('}');
        }
        else
        s.push_back(s[i]);
    }

    stack < unordered_set< string>> stackStr;
    stack <int> stackOp;
    unordered_set<string> curStr;

    for(int i =0; i < s.size();i++){
        if(s[i]=='{'){
            stackStr.push(cur);
            stackOp.push(0);
            cur= {};
        }else if(s[i] ==','){
            stackStr.push(cur);
            stackOp.push(1);
            cur= {};
        }else if(s[i] == '}'){
            while(stackOp.top() == 1){
                cur = combine(stack.top(),cur);
                stackOp.pop();
                stackStr.pop();
            }
            if(stackOp.top() == 0){
                cur = cossProduct(stack.top(),cur);
                stackOp.pop();
                stackStr.pop();
            }
        }else{
            string temp;
            temp.push_back(s[i])
            cur.push_back(temp);
        }
    }
    vector<string> rets(cur.begin(),cur.end());
    sort(rets.begin(),rets.end());
    return rets;
}