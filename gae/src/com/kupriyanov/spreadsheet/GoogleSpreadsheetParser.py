
import logging


def getRowValue(row, format, column_name):
    logging.info('getRowValue[%s]:%s' % (column_name, row))
    
    if str(column_name) == '':
        raise ValueError('column_name must not empty')
        
    begin = row.find('%s:' % column_name)
    
    logging.info('begin:%s' % begin)
       
    if begin == -1:
        return ''
    
    begin = begin + len(column_name) + 1
    
       
    end = -1
    found_begin = False
    
    for entity in format:
        logging.info('checking:%s' % entity)
        
        if found_begin and row.find(entity) != -1:
            end = row.find(entity)
            break
        
        if entity == column_name:
            found_begin = True
    
    
    #check if last element
    if format[len(format) -1 ] == column_name:
        end = len(row)
    else:
        if end == -1:
            end = len(row)
        else:
            end = end - 2
        
    logging.info('%s:%s' % (column_name, row) )
    #logging.info('speakertitle[%s]' % speaker_title )
    #logging.info('%s:%s' % (column_name, row.find(column_name)))
#        logging.info('%s - %s' % (begin, end))
    
    value = row[begin: end].strip()
    
    logging.info('%s[%s-%s]:[%s]' % (column_name, begin, end, value))
    

    return value