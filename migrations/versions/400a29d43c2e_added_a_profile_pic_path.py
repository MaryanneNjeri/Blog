"""added a profile-pic path

Revision ID: 400a29d43c2e
Revises: 2bf59c24ffce
Create Date: 2018-04-22 23:20:11.956352

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '400a29d43c2e'
down_revision = '2bf59c24ffce'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('posts', sa.Column('profile_pic_path', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('posts', 'profile_pic_path')
    # ### end Alembic commands ###
