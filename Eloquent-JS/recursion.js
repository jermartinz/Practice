function itsEven(number) {
    if (number % 2 === 0) {
        return true;
        
    }
    else if (number % 2 === 1){
        
        return false;
    }else {
        return number -2;
    }
    
}

console.log(itsEven(50));
console.log(itsEven(75));
console.log(itsEven(-1));