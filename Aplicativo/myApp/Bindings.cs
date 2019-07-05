namespace Ninject
{   
    using System;
    using Ninject;
    using Ninject.Modules;

    public class Bindings : NinjectModule
    {
        public override void Load()
        {
            //Bind<IMailSender>().To<MockMailSender>();
            Bind<IMailSender>().To<MailSender>();
        }

    }    
}
