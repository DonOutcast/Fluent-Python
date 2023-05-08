symbols = '$¢£¥€¤'
m_tuple = tuple(ord(symbol) for symbol in symbols)
print(m_tuple)
import array
m_array = array.array("I", (ord(symbol) for symbol in symbols))
print(m_array)
