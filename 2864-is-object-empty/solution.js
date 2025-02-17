/**
 * @param {Object|Array} obj
 * @return {boolean}
 */
var isEmpty = function(obj) {
    for (let key in obj)
        return false;
    return true;

    //no need of two if cases easy only
    
};
