namespace Assn3Template
{
    partial class Form1
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.btnOneIteration = new System.Windows.Forms.Button();
            this.numOfIteration = new System.Windows.Forms.NumericUpDown();
            this.btnMultiIteration = new System.Windows.Forms.Button();
            ((System.ComponentModel.ISupportInitialize)(this.numOfIteration)).BeginInit();
            this.SuspendLayout();
            // 
            // btnOneIteration
            // 
            this.btnOneIteration.Location = new System.Drawing.Point(27, 452);
            this.btnOneIteration.Name = "btnOneIteration";
            this.btnOneIteration.Size = new System.Drawing.Size(142, 50);
            this.btnOneIteration.TabIndex = 0;
            this.btnOneIteration.Text = "Run One Iteration";
            this.btnOneIteration.UseVisualStyleBackColor = true;
            this.btnOneIteration.Click += new System.EventHandler(this.btnOneIteration_Click);
            // 
            // numOfIteration
            // 
            this.numOfIteration.Location = new System.Drawing.Point(175, 452);
            this.numOfIteration.Name = "numOfIteration";
            this.numOfIteration.Size = new System.Drawing.Size(120, 22);
            this.numOfIteration.TabIndex = 1;
            // 
            // btnMultiIteration
            // 
            this.btnMultiIteration.Location = new System.Drawing.Point(301, 452);
            this.btnMultiIteration.Name = "btnMultiIteration";
            this.btnMultiIteration.Size = new System.Drawing.Size(149, 50);
            this.btnMultiIteration.TabIndex = 2;
            this.btnMultiIteration.Text = "Run Multiple Iteration";
            this.btnMultiIteration.UseVisualStyleBackColor = true;
            this.btnMultiIteration.Click += new System.EventHandler(this.btnMultiIteration_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(479, 554);
            this.Controls.Add(this.btnMultiIteration);
            this.Controls.Add(this.numOfIteration);
            this.Controls.Add(this.btnOneIteration);
            this.Margin = new System.Windows.Forms.Padding(4);
            this.Name = "Form1";
            this.Text = "Form1";
            this.Load += new System.EventHandler(this.Form1_Load);
            ((System.ComponentModel.ISupportInitialize)(this.numOfIteration)).EndInit();
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.Button btnOneIteration;
        private System.Windows.Forms.NumericUpDown numOfIteration;
        private System.Windows.Forms.Button btnMultiIteration;
    }
}

