using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ThermoMeter
{
    /// <summary>
    /// Tester
    /// </summary>
    class Program
    {
        /// <summary>
        /// Read setting from config
        /// </summary>
        /// <returns>ThermoRecord with setting values.</returns>
        static ThermoRecord ReadConfig()
        {
            string freezingStr = HelperAdapter.GetProperty("freezing");
            string boilingStr = HelperAdapter.GetProperty("boiling");
            string flunctuationStr = HelperAdapter.GetProperty("fluctuating");
            ThermoItem freezingThermo = ThermoItem.getThermo(freezingStr);
            ThermoItem boilingThermo = ThermoItem.getThermo(boilingStr);
            ThermoItem flunctuationThermo = ThermoItem.getThermo(flunctuationStr);
            ThermoRecord thermoRecord = new ThermoRecord(boilingThermo.GetThermoInCels(), freezingThermo.GetThermoInCels(), 
                flunctuationThermo.GetThermoInCels());
            return thermoRecord;
        }

        /// <summary>
        /// Start the test
        /// </summary>
        /// <param name="args">No Args needs</param>
        static void Main(string[] args)
        {
            ThermoRecord thermoRecord= ReadConfig();
            string ordIn = Console.ReadLine();
            while (ordIn.Length != 0) 
            {
                try
                {
                    ThermoItem item = ThermoItem.getThermo(ordIn);
                    Console.WriteLine(item);
                    thermoRecord.AddRecord(item);
                }
                catch (Exception ex) 
                {
                    Console.WriteLine(ex.Message);
                }
                ordIn = Console.ReadLine();
            }    
        }
    }

   
}
