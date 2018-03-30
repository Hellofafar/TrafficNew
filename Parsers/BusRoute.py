class BusRoute:
    def __init__(self, agency, record):
        self.__routeId = int(record[0])
        self.__routeDes = record[1]
        temp = record[2].split(',')
        self.__zones = [0 for i in range(len(temp))]
        for i in range(len(temp)):
            try:
                self.__zones[i] = int(temp[i])
            except:
                self.__zones[i] = -1
        self.__agency = agency

            
        public BusRoute(string agency, List<string> record)
        {
            _routeId = Int32.Parse(record[0]);
            _routeDes = record[1];
            String[] temp = record[2].Split(',');
            _zones = new int[temp.Length];
            for (int i = 0; i < temp.Length; i++)
            {
                try
                {
                    _zones[i] = Convert.ToInt16(temp[i]);
                }
                catch (Exception)
                {
                    _zones[i] = -1;
                }
            }
            _agency = agency;
        }