Give me code for hello world in c#

Here is the code for a simple \"Hello World\" program in C# using the Console application template:

```csharp
using System;

namespace HelloWorld
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(\"Hello World!\");
        }
    }
}
```

To run the program, save it in a file with the extension `.cs` (for example, `HelloWorld.cs`), and then use the `dotnet` command-line tool or Visual Studio to compile and run it.

For example, if you have installed the .NET SDK, you can compile and run the program from the command line as follows:

```bash
dotnet new console -o HelloWorld
dotnet run HelloWorld.cs
```

Or, if you prefer using Visual Studio, you can create a new Console App project, replace the contents of the `Program.cs` file with the code above, and then press F5 to run the program.