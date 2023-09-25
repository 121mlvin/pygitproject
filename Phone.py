class Phone:
    phone_number = '956870498'
    _incoming_calls_counter = 0
    _incoming_calls_data = []

    def set_phone_num(self, num):
        self.phone_number = num
        return 'Your phone number is {}'.format(self.phone_number)

    def get_incoming_call(self, num):
        self._incoming_calls_counter += 1
        self._incoming_calls_data.append(num)
        return 'Incoming call from: {}'.format(num)

    def get_incoming_calls_count(self):
        return 'All amount of incoming calls: {}'.format(self._incoming_calls_counter)


phone1 = Phone()
print(phone1.set_phone_num('124124124'))
print(phone1.get_incoming_call('23523234'))
print(phone1.get_incoming_call('2356756823234'))
print(phone1.get_incoming_call('5685623523234'))
print(phone1.get_incoming_calls_count())

phone2 = Phone()
print(phone2.set_phone_num('6345820'))
print(phone2.get_incoming_call('23523234245'))
print(phone2.get_incoming_call('235232334534'))
print(phone2.get_incoming_call('235265473234'))
print(phone2.get_incoming_call('235273234'))
print(phone2.get_incoming_call('4857689346'))
print(phone2.get_incoming_calls_count())

phone3 = Phone()
print(phone3.set_phone_num('56758464'))
print(phone3.get_incoming_call('02462356'))
print(phone3.get_incoming_call('273658723'))
print(phone3.get_incoming_calls_count())


def all_phones_incoming_calls(phones):
    result = []
    for i in phones:
        result.append(int(i.get_incoming_calls_count()[30:]))
    f = open("text1.csv", 'w')
    f.write(', '.join(i._incoming_calls_data) +
            '\nall amount of calls: ' +
            str(sum(result)))
    f.close()

    return f'The amount of all calls from all phones: {sum(result)}'

print(all_phones_incoming_calls([phone1, phone2, phone3]))