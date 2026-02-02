type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    let ans = []
    let c = 0
    while (c<arr.length){
        ans.push(arr.slice(c,c+size))
        c+=size
    }
    
    return ans
};

