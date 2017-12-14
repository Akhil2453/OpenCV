# Installing steps for anaconda in Linux


Installing on Linux

For x86 systems.

    In your browser, download the Anaconda installer for Linux.

    Optional: Verify data integrity with MD5 or SHA-256. (For more information on hashes, see cryptographic hash validation.)

        Run the following:

        md5sum /path/filename

        OR:

        sha256sum /path/filename

        NOTE: Replace /path/filename with the actual path and filename of the file you downloaded.

        Optional: Verify results against the proper hash page to make sure the hashes match.

    Enter the following to install Anaconda for Python 3.6:

    bash ~/Downloads/Anaconda3-5.0.1-Linux-x86_64.sh

    OR Enter the following to install Anaconda for Python 2.7:

    bash ~/Downloads/Anaconda2-5.0.1-Linux-x86_64.sh

    NOTE: Include the bash command regardless of whether or not you are using Bash shell.

    NOTE: If you did not download to your Downloads directory, replace ~/Downloads/ with the path to the file you downloaded.

    NOTE: Choose “Install Anaconda as a user” unless root privileges are required.

    The installer prompts “In order to continue the installation process, please review the license agreement.” Click Enter to view license terms.

    Scroll to the bottom of the license terms and enter “Yes” to agree.

    The installer prompts you to click Enter to accept the default install location, CTRL-C to cancel the installation, or specify an alternate installation directory. If you accept the default install location, the installer displays “PREFIX=/home/<user>/anaconda<2 or 3>” and continues the installation. It may take a few minutes to complete.

    The installer prompts “Do you wish the installer to prepend the Anaconda<2 or 3> install location to PATH in your /home/<user>/.bashrc ?” Enter Yes.

    NOTE: If you enter “No”, you must manually add the path to Anaconda or conda will not work. See FAQ.

    The installer finishes and displays “Thank you for installing Anaconda<2 or 3>!”

    Close and open your terminal window for the installation to take effect, or you can enter the command source ~/.bashrc.

    After your install is complete, verify it by opening Anaconda Navigator, a program that is included with Anaconda: Open a Terminal window and type anaconda-navigator. If Navigator opens, you have successfully installed Anaconda. If not, check that you completed each step above, then see our Help page.

    TIP: Anaconda Navigator contains Jupyter Notebook and the Spyder IDE. For more information about Navigator, see Navigator.

After your install completes, start using Anaconda with the instructions in Getting started.

NOTE: If you install multiple versions of Anaconda, the system defaults to the most current version, as long as you haven’t altered the default install path.
