class Bank {
    private balance: number[];
    private n: number;

    constructor(balance: number[]) {
        this.balance = balance;
        this.n = balance.length;
    }

    transfer(account1: number, account2: number, money: number): boolean {
        if (account1 <= 0 || account1 > this.n ||
            account2 <= 0 || account2 > this.n)
            return false;
        if (this.balance[account1 - 1] < money)
            return false;
        this.balance[account1 - 1] -= money;
        this.balance[account2 - 1] += money;
        return true;
    }

    deposit(account: number, money: number): boolean {
        if (account <= 0 || account > this.n)
            return false;
        this.balance[account - 1] += money;
        return true;
    }

    withdraw(account: number, money: number): boolean {
        if (account <= 0 || account > this.n || this.balance[account - 1] < money)
            return false;
        this.balance[account - 1] -= money;
        return true;
    }
}
