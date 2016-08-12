yuanyin=set('aeiouAEIOU');
letters=set([chr(i) for i in range(97,123)]+[chr(i) for i in range(65,91)]);
not_yuanyin=letters-yuanyin;

sentence="And the lord spake, saying: First shalt thou take out the Holy Pin.";
print len(sentence);
print "The words count is %d"%len(sentence.split());
print "The count of yuanyin is %d"%len([letter for letter in sentence if letter in yuanyin]);
print "The count of fuyin is %d"%len([letter1 for letter1 in sentence if letter1 in not_yuanyin])