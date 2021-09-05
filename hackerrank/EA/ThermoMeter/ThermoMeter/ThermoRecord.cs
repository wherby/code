using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace ThermoMeter
{
    /// <summary>
    /// State machine for alert.
    /// </summary>
    class ThermoRecord
    {
        enum RecordStatus {Init, Freezed, Boiled, Normal};
        private float upperTrigger;
        private float downerTriggrt;
        private float flunctuating;
        private RecordStatus status;
        private IMyAlert iMyAlert;

        /// <summary>
        /// New a state machine of record to send alert message.
        /// </summary>
        /// <param name="upper">High vlaue for alert.</param>
        /// <param name="down">Low value for alert.</param>
        /// <param name="flunt">Fluntuating value for alert.</param>
        public ThermoRecord(float upper, float down, float flunt)
        {
            upperTrigger = upper;
            downerTriggrt = down;
            flunctuating = flunt;
            status = RecordStatus.Init;
            iMyAlert = new ThemoAlert();
        }

        /// <summary>
        /// The logic of the alert:
        ///  1. In start, if not in normal status, no alert.
        ///  2. If in normal status, then enter abnormal status, alert.
        ///  3. If in abnormal status, then enter another abnormal status, alert.
        ///  4, If in abnormal status, then will have flunctuating to reenter normal status.
        /// </summary>
        /// <param name="item"></param>
        public void AddRecord(ThermoItem item) 
        {
            float t = item.GetThermoInCels();
            if (status == RecordStatus.Init)
            {
                if (t <= downerTriggrt)
                {
                    status = RecordStatus.Freezed;
                }
                else if (t >= upperTrigger)
                {
                    status = RecordStatus.Boiled;
                }
                else
                {
                    status = RecordStatus.Normal;
                }
            }
            else 
            {
                if (status == RecordStatus.Normal) 
                {
                    if (t <= downerTriggrt)
                    {
                        status = RecordStatus.Freezed;
                        iMyAlert.Alert("Freezing");
                    }
                    else if (t >= upperTrigger)
                    {
                        status = RecordStatus.Boiled;
                        iMyAlert.Alert("Boiling");
                    }
                    else
                    {
                        status = RecordStatus.Normal;
                    }
                }
                if (status == RecordStatus.Boiled)
                {
                    if (t <= downerTriggrt)
                    {
                        status = RecordStatus.Freezed;
                        iMyAlert.Alert("Freezing");
                    }
                    else if (t >= upperTrigger - flunctuating)
                    {
                        status = RecordStatus.Boiled;
                    }
                    else
                    {
                        status = RecordStatus.Normal;
                    }
                }
                if (status == RecordStatus.Freezed)
                {
                    if (t <= downerTriggrt + flunctuating)
                    {
                        status = RecordStatus.Freezed;
                    }
                    else if (t >= upperTrigger)
                    {
                        status = RecordStatus.Boiled;
                        iMyAlert.Alert("Boiling");
                    }
                    else
                    {
                        status = RecordStatus.Normal;
                    }
                }
            }
        }
    }

    interface IMyAlert
    {
        void Alert(string msg);
    }

    class ThemoAlert : IMyAlert 
    {
        /// <summary>
        /// Simply output alert.
        /// </summary>
        /// <param name="msg"> Alert message.</param>
        public void Alert(string msg) 
        {
            Console.WriteLine("Alert: {0} !!!", msg);
        }
    }
}
