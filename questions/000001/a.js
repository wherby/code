fq  =function f(a){
    console.log(a);
}

f2 = function(b){
    return function f3(a){
        console.log(a);
        console.log(b);
    };
}
fq("a")
f3= f2("c")
f3("d")