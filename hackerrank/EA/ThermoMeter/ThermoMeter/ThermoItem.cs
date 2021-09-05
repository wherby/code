using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ThermoMeter
{
    /// <summary>
    /// Thermo item only maintains Cels degrade.
    /// </summary>
    class ThermoItem
    {
        private float thermoInCels;

        /// <summary>
        /// Getter for thermoInCels.
        /// </summary>
        /// <returns>Value of thermoInCels.</returns>
        public float GetThermoInCels()
        {
            return thermoInCels;
        }

        /// <summary>
        /// 
        /// </summary>
        /// <param name="num">Value for Cels.</param>
        public ThermoItem(float num)
        {
            if (num < -273.15) 
            {
                // Lowest temperature
                Console.WriteLine("Can't be lower than -273.15 C. So set it to  -273.15 C .");
                num = (float)-273.15;
            }
            thermoInCels = num;
        }

        /// <summary>
        /// Get input string change to Celsius 
        /// </summary>
        /// <param name="thermoStr"> input string of temperature, which allows both "50C","40 C", "45 F","556F" and so on.</param>
        /// <returns>The TheroItem contains Cels value.</returns>
        public static ThermoItem getThermo(string thermoStr)
        {
            if (thermoStr.Contains("C"))
            {
                String[] splitV = thermoStr.Trim().Split('C');
                float num;
                bool success = float.TryParse(splitV[0], out num);
                if (success == true && splitV[1] == "")
                {
                    ThermoItem t1 = new ThermoItem(num);
                    return t1;
                }
                else
                {
                    throw new Exception("Not a valid format of ceisius for : " + thermoStr);
                }
            };
            if (thermoStr.Contains("F"))
            {
                String[] splitV = thermoStr.Trim().Split('F');
                float num;
                bool success = float.TryParse(splitV[0], out num);
                if (success == true && splitV[1] == "")
                {
                    num = (num - 32) * 5 / 9;
                    ThermoItem t1 = new ThermoItem(num);
                    return t1;
                }
                else
                {
                    throw new Exception("Not a valid format of Fahrenheit for : " + thermoStr);
                }
            }
            throw new Exception("Not a valid input : " + thermoStr);
        }

        /// <summary>
        /// String format of  ThermoItem
        /// </summary>
        /// <returns>Both Celsius and Fahrenheit vaule.</returns>
        public override string ToString()
        {
            float thermoInFahren = thermoInCels * 9 / 5 + 32;
            string reStr = string.Format("The temperature is {0:0.0} F and {1:0.0} C ", thermoInFahren, thermoInCels);
            return reStr;
        }
    }
}
