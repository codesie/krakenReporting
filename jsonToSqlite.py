import json
import datetime

from db.handle import create_tables, insert_new_trade


def main():
    """
    Main function of the script. Gets all trades and consolidates the data.

    logger (logging): logging handler for writing to the log file
    """
    json_file = open("logs/trades.json", "r")

    create_tables()

    trades = json.load(json_file)

    for trade in trades:
        trade_id = trade
        order_id = trades[trade]["ordertxid"]
        pair = trades[trade]["pair"]
        executed = datetime.datetime.fromtimestamp(trades[trade]["time"]).isoformat()
        direction_type = trades[trade]["type"]
        order_type = trades[trade]["ordertype"]
        price = trades[trade]["price"]
        cost = trades[trade]["cost"]
        if direction_type == "buy":
            cost = float(cost) * -1
        fee = float(trades[trade]["fee"]) * -1
        volume = trades[trade]["vol"]
        if direction_type == "sell":
            volume = float(volume) * -1

        data = (trade_id, order_id, pair, executed, direction_type, order_type, price, cost, fee, volume)
        # print(data)
        insert_new_trade(data)


if __name__ == "__main__":
    """
    Main entry of the script. First, the provided arguments are parsed and then the main purpose of the script is 
    executed.
    """
    main()
