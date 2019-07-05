namespace Ninject
{   
    using System;
    using Ninject;  

    class Program
    {
        static void Main(string[] args)
        {
            /* IMailSender mailSender = new MockMailSender();
            FormHandler formHandler = new FormHandler(mailSender);
            formHandler.Handle("nsanabiom@uni.pe");
            Console.ReadLine();*/

            var kernel = new StandardKernel();
            kernel.Load(System.Reflection.Assembly.GetExecutingAssembly());
            
            var mailSender = kernel.Get<IMailSender>();

            var formHandler = new FormHandler(mailSender);
            formHandler.Handle("nsanabiom@uni.pe");

            Console.ReadLine();
    }
}    
}
