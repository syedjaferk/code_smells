class Address:
    def __init__(self, city, post_code, country):
        self._city = city
        self._post_code = post_code
        self._country = country
    
    def get_city(self):
        return self._city
    
    def set_city(self, city):
        self._city = city
    
    def get_post_code(self):
        return self._post_code
    
    def set_post_code(self, post_code):
        self._post_code = post_code
    
    def get_country(self):
        return self._country
    
    def set_country(self, country):
        self._country = country


class Customer:
    def __init__(self, address, title, name):
        self._address = address
        self._title = title
        self._name = name
    
    def get_address(self):
        return self._address
    
    def set_address(self, address):
        self._address = address
    
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        self._title = title

    def get_name(self):
        return self._name
    
    def set_name(self, name):
        self._name = name


class CustomerSummaryView:
    def __init__(self, customer):
        self.customer = customer
    
    def get_customer_summary(self):
        address = self.customer.get_address()
        return self.customer.get_title() + " " + self.customer.get_name() + " " + address.get_post_code() + " " + address.get_country()


# Test

if __name__ == "__main__":
    address = Address(city="Chennai", post_code="600048", country="India")
    customer = Customer(address=address, title="Mr.", name="Syed Jafer")
    customer_summary_view = CustomerSummaryView(customer=customer)
    print(customer_summary_view.get_customer_summary())