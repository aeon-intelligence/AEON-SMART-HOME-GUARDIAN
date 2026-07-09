class InventoryAvailability:

    def available(self,
                  on_hand,
                  reserved):

        return max(0, on_hand - reserved)
