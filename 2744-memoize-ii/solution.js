/**
 * @param {Function} fn
 * @return {Function}
 */
function memoize(fn) {
    
    const memo = new Map();

    return function (...args) {
        let node = memo;

        for (let arg of args) {
            node.has(arg) || node.set(arg, new Map());
            node = node.get(arg);
        }

        if (node.has("savedResult")) {
            return node.get("savedResult");
        }

        const result = fn(...args);
        node.set("savedResult", result);
        return result;
    };
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */
