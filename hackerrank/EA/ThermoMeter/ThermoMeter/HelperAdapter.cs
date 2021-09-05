using System.Collections.Generic;
using System.Configuration;
using System;
using System.Text;
using System.Text.RegularExpressions;
using System.Xml;
using System.Xml.Serialization;
using System.Xml.XPath;
using System.Web;
using System.IO;

namespace ThermoMeter
{
    class HelperAdapter
    {
        /// <summary>
        /// The method is used to get value from configure file.
        /// </summary>
        /// <param name="propertyName">The name of property.</param>
        /// <returns>The value of property.</returns>
        public static string GetProperty(string propertyName)
        {
            string propertyValue = ConfigurationManager.AppSettings[propertyName];
            if (propertyValue == null)
            {
                Exception ex = new Exception(string.Format("The property {0} is not exist in configure file", propertyName));
                throw ex;
            }
            return propertyValue;
        }
    }
}
